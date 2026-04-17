"""
AfyaMkononi SMS Route v3.0
Handles incoming SMS - conversational, accurate, with severity levels.
"""

from fastapi import APIRouter, Form
from fastapi.responses import PlainTextResponse, JSONResponse
import logging

from services.sms_parser import parse
from services.ai_engine import ask_gemini
from services.at_sms import send_sms
from services.health_data import get_severity
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
    """Handle incoming SMS from Africa's Talking callback."""
    try:
        logger.info(f"SMS received: from={sender}, to={to}, text={text}")
        
        if not text:
            logger.warning("SMS received with no text")
            return JSONResponse({"status": "error", "message": "No text received"})
        
        if not sender:
            logger.warning("SMS received with no sender")
            return JSONResponse({"status": "error", "message": "No sender"})
            
        parsed = parse(text.strip())
        lang   = parsed["lang"]
        disease = parsed.get("disease")
        
        logger.info(f"Parsed: lang={lang}, emergency={parsed['is_emergency']}, disease={disease}")

        # Determine reply and severity
        if parsed["is_emergency"]:
            reply = parsed["response"]
            severity = "red"
        elif parsed.get("is_greeting"):
            reply = parsed["response"]
            severity = "green"
        elif parsed.get("is_help"):
            reply = parsed["response"]
            severity = "green"
        elif parsed["use_ai"]:
            # Use AI for health questions
            reply = await ask_gemini(text.strip(), lang)
            # Determine severity from text and reply
            severity = _determine_severity(text, reply, disease)
        else:
            reply = parsed["response"]
            severity = _determine_severity(text, reply, disease)

        # Log consultation
        await _log(sender, lang, disease, severity, reply)
        
        # Send reply
        sent = await send_sms(sender, reply)
        
        if sent:
            logger.info(f"SMS sent to {sender} | severity={severity}")
            return JSONResponse({"status": "success", "message": "Reply sent", "severity": severity})
        else:
            logger.error(f"Failed to send SMS to {sender}")
            return JSONResponse({"status": "error", "message": "Failed to send reply"})
        
    except Exception as e:
        logger.error(f"SMS error: {e}", exc_info=True)
        return JSONResponse({"status": "error", "message": str(e)})


def _determine_severity(user_text: str, reply_text: str, disease: str = None) -> str:
    """
    Determine severity level: red, yellow, green.
    
    RED = Emergency - hospital NOW
    YELLOW = Urgent - visit clinic today
    GREEN = Not urgent - rest and monitor
    """
    text_combined = (user_text + " " + reply_text).upper()
    
    # RED indicators - emergency
    red_keywords = [
        "DHARURA", "EMERGENCY", "HOSPITALI SASA", "HOSPITAL NOW",
        "HARAKA", "FAST", "SASA HIVI", "RIGHT NOW",
        "HATARI", "DANGER", "KIHARUSI", "STROKE",
        "DEGEDEGE", "SEIZURE", "FAHAMU", "UNCONSCIOUS",
        "DAMU NYINGI", "HEAVY BLEEDING"
    ]
    
    for keyword in red_keywords:
        if keyword in text_combined:
            return "red"
    
    # Check disease-specific severity
    if disease:
        disease_severity = get_severity(disease, user_text)
        if disease_severity == "red":
            return "red"
    
    # YELLOW indicators - needs clinic visit
    yellow_keywords = [
        "FIKA", "VISIT", "PIMA", "TEST", "CHECK",
        "KITUO CHA AFYA", "HEALTH CENTER", "CLINIC",
        "HOSPITALI", "HOSPITAL", "DAKTARI", "DOCTOR"
    ]
    
    for keyword in yellow_keywords:
        if keyword in text_combined:
            return "yellow"
    
    # GREEN - rest and monitor
    return "green"


async def _log(phone, lang, disease, severity, advice):
    """Log consultation to database."""
    try:
        save_consultation(
            phone=phone,
            channel="sms",
            lang=lang,
            disease=disease,
            severity=severity,
            advice_given=advice,
        )
    except Exception as e:
        logger.warning(f"Failed to log consultation: {e}")
