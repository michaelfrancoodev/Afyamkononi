from fastapi import APIRouter, Form
from fastapi.responses import PlainTextResponse
import logging

from services.sms_parser import parse
from services.ai_engine import ask_gemini
from database.queries import save_consultation

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/sms", response_class=PlainTextResponse)
async def sms_handler(
    sender: str = Form(None, alias="from"),
    to:     str = Form(None),
    text:   str = Form(None),
    date:   str = Form(""),
):
    try:
        logger.info(f"SMS request: from={sender}, to={to}, text={text}")
        
        # Validate required fields
        if not text:
            return PlainTextResponse("Tafadhali tuma ujumbe wako. Mfano: nina homa kali")
        
        if not sender:
            sender = "unknown"
            
        parsed = parse(text.strip())
        lang   = parsed["lang"]

        if parsed["is_emergency"]:
            reply = parsed["response"]
            await _log(sender, lang, None, "red", reply)
            return PlainTextResponse(reply)

        if parsed["use_ai"]:
            reply = await ask_gemini(text, lang)
        else:
            reply = parsed["response"]

        disease  = parsed.get("disease")
        severity = _guess_severity(reply)

        await _log(sender, lang, disease, severity, reply)
        return PlainTextResponse(reply)
        
    except Exception as e:
        logger.error(f"SMS error: {e}", exc_info=True)
        return PlainTextResponse("Samahani, kuna tatizo la kiufundi. Tafadhali jaribu tena baadaye.")


def _guess_severity(text: str) -> str:
    t = text.upper()
    if "DHARURA" in t or "EMERGENCY" in t:
        return "red"
    if "USHAURI" in t or "ADVICE" in t or "FIKA" in t:
        return "yellow"
    return "green"


async def _log(phone, lang, disease, severity, advice):
    try:
        save_consultation(
            phone=phone,
            channel="sms",
            lang=lang,
            disease=disease,
            severity=severity,
            advice_given=advice,
        )
    except Exception:
        pass
