from fastapi import APIRouter, Form
from fastapi.responses import PlainTextResponse

from services.sms_parser import parse
from services.ai_engine import ask_gemini
from database.queries import save_consultation

router = APIRouter()


@router.post("/sms", response_class=PlainTextResponse)
async def sms_handler(
    sender: str = Form(..., alias="from"),
    to:     str = Form(...),
    text:   str = Form(...),
    date:   str = Form(""),
):
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
