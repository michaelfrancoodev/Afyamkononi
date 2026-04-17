from fastapi import APIRouter, Form
from fastapi.responses import PlainTextResponse, JSONResponse
import logging

from services.sms_parser import parse
from services.ai_engine import ask_gemini
from services.at_sms import send_sms
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
    """Handle incoming SMS from Africa's Talking callback.
    
    Africa's Talking sends incoming SMS to this endpoint.
    We process the message and send a reply via the AT SMS API.
    """
    try:
        logger.info(f"SMS received: from={sender}, to={to}, text={text}")
        
        # Validate required fields
        if not text:
            logger.warning("SMS received with no text")
            return JSONResponse({"status": "error", "message": "No text received"})
        
        if not sender:
            logger.warning("SMS received with no sender")
            return JSONResponse({"status": "error", "message": "No sender"})
            
        parsed = parse(text.strip())
        lang   = parsed["lang"]
        
        logger.info(f"Parsed SMS: lang={lang}, emergency={parsed['is_emergency']}, greeting={parsed.get('is_greeting', False)}")

        # Determine reply based on parse results
        if parsed["is_emergency"]:
            reply = parsed["response"]
            severity = "red"
        elif parsed.get("is_greeting"):
            reply = parsed["response"]
            severity = "green"
        elif parsed["use_ai"]:
            reply = await ask_gemini(text.strip(), lang)
            severity = _guess_severity(reply)
        else:
            reply = parsed["response"]
            severity = _guess_severity(reply)

        disease = parsed.get("disease")

        await _log(sender, lang, disease, severity, reply)
        
        # Send reply via Africa's Talking SMS API
        sent = await send_sms(sender, reply)
        
        if sent:
            logger.info(f"SMS reply sent to {sender}")
            return JSONResponse({"status": "success", "message": "Reply sent"})
        else:
            logger.error(f"Failed to send SMS reply to {sender}")
            return JSONResponse({"status": "error", "message": "Failed to send reply"})
        
    except Exception as e:
        logger.error(f"SMS error: {e}", exc_info=True)
        return JSONResponse({"status": "error", "message": str(e)})


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
