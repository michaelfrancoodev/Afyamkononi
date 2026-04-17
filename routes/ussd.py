from fastapi import APIRouter, Form
from fastapi.responses import PlainTextResponse
import logging

import services.session as session_store
from services.triage import triage, needs_q2
from core.languages import screen, result, exit_screen
from core.constants import CON, END, LANG_SW, LANG_EN, MALARIA, PNEUMONIA, DIARRHEA, BP, OTHER
from database.queries import save_consultation

router = APIRouter()
logger = logging.getLogger(__name__)

DISEASE_MAP = {
    "1": MALARIA,
    "2": PNEUMONIA,
    "3": DIARRHEA,
    "4": BP,
    "5": OTHER,
}


def format_response(rtype: str, msg: str) -> str:
    """Format USSD response for Africa's Talking.
    
    Africa's Talking expects: 'CON message' or 'END message' (space, not newline)
    """
    return f"{rtype} {msg}"


@router.post("/ussd", response_class=PlainTextResponse)
async def ussd_handler(
    sessionId:   str = Form(...),
    phoneNumber: str = Form(...),
    text:        str = Form(""),
    serviceCode: str = Form(""),
):
    try:
        logger.info(f"USSD request: sessionId={sessionId}, phone={phoneNumber}, text={text}")
        
        # Africa's Talking sends all inputs joined by * e.g. "1*2*1"
        steps = [s for s in text.split("*") if s]
        sess  = session_store.get_or_create(sessionId, phoneNumber)

        lang = LANG_EN if (steps and steps[0] == "2") else LANG_SW
        sess.lang = lang

        # Exit from anywhere
        if steps and steps[-1] == "0":
            session_store.delete(sessionId)
            rtype, msg = exit_screen(lang)
            return PlainTextResponse(format_response(rtype, msg))

        # Welcome screen - no input yet
        if not steps:
            rtype, msg = screen("welcome", LANG_SW)
            return PlainTextResponse(format_response(rtype, msg))

        # Step 1 - language chosen, show main menu
        if len(steps) == 1:
            session_store.update(sess)
            rtype, msg = screen("main", lang)
            return PlainTextResponse(format_response(rtype, msg))

        # Step 2 - disease chosen, show Q1
        if len(steps) == 2:
            disease = DISEASE_MAP.get(steps[1])

            if not disease or disease == OTHER:
                session_store.delete(sessionId)
                rtype, msg = result("other", OTHER, lang)
                await _log(phoneNumber, sess, OTHER, None, msg)
                return PlainTextResponse(format_response(rtype, msg))

            sess.disease = disease
            session_store.update(sess)
            rtype, msg = screen(f"{disease}_q1", lang)
            return PlainTextResponse(format_response(rtype, msg))

        # Step 3 - Q1 answered
        if len(steps) == 3:
            disease = DISEASE_MAP.get(steps[1])
            if not disease:
                session_store.delete(sessionId)
                rtype, msg = result("other", OTHER, lang)
                return PlainTextResponse(format_response(rtype, msg))

            q1 = steps[2]

            # BP + q1=yes means stroke signs - go straight to RED, no Q2 needed
            if disease == BP and q1 == "1":
                severity = triage(disease, q1)
                session_store.delete(sessionId)
                rtype, msg = result(severity, disease, lang)
                await _log(phoneNumber, sess, disease, severity, msg)
                return PlainTextResponse(format_response(rtype, msg))

            # All other cases - ask Q2
            sess.disease = disease
            sess.q1      = q1
            session_store.update(sess)
            rtype, msg = screen(f"{disease}_q2", lang)
            return PlainTextResponse(format_response(rtype, msg))

        # Step 4 - Q2 answered, give final result
        if len(steps) >= 4:
            disease = DISEASE_MAP.get(steps[1])
            if not disease:
                session_store.delete(sessionId)
                rtype, msg = result("other", OTHER, lang)
                return PlainTextResponse(format_response(rtype, msg))

            q1       = steps[2]
            q2       = steps[3]
            severity = triage(disease, q1, q2)
            session_store.delete(sessionId)
            rtype, msg = result(severity, disease, lang)
            await _log(phoneNumber, sess, disease, severity, msg)
            return PlainTextResponse(format_response(rtype, msg))

        session_store.delete(sessionId)
        rtype, msg = exit_screen(lang)
        return PlainTextResponse(format_response(rtype, msg))
        
    except Exception as e:
        logger.error(f"USSD error: {e}", exc_info=True)
        # Always return a valid response even on error
        return PlainTextResponse("END Samahani, kuna tatizo la kiufundi. Tafadhali jaribu tena baadaye.")


async def _log(phone, sess, disease, severity, advice):
    try:
        save_consultation(
            phone=phone,
            channel=sess.channel,
            lang=sess.lang,
            disease=disease,
            severity=severity,
            advice_given=advice,
        )
    except Exception:
        pass
