from services.health_data import classify_sms_keywords
from core.constants import LANG_SW, LANG_EN

RED_FLAG_WORDS_SW = [
    "fahamu", "kuanguka", "degedege", "mshtuko",
    "kushindwa kupumua", "damu nyingi",
]
RED_FLAG_WORDS_EN = [
    "unconscious", "fainted", "seizure", "convulsion",
    "not breathing", "heavy bleeding",
]

EMERGENCY_SW = (
    "DHARURA!\n"
    "Dalili hizi ni hatari.\n"
    "Nenda hospitali SASA.\n"
    "Usisubiri. Kila dakika\nni muhimu kuokoa maisha."
)
EMERGENCY_EN = (
    "EMERGENCY!\n"
    "These symptoms are dangerous.\n"
    "Go to hospital NOW.\n"
    "Do not wait. Every minute matters."
)

UNKNOWN_SW = (
    "Tumepokea ujumbe wako.\n"
    "Dalili hizi hazitambuliwi.\n"
    "Kwa usalama wako,\nfika kituo cha afya\nkilicho karibu nawe."
)
UNKNOWN_EN = (
    "We received your message.\n"
    "We could not identify those symptoms.\n"
    "For your safety, visit the\nnearest health center."
)


def detect_language(text: str) -> str:
    en_markers = ["fever", "cough", "pain", "help", "sick", "vomit", "diarrhea", "blood"]
    text_lower = text.lower()
    count = sum(1 for w in en_markers if w in text_lower)
    return LANG_EN if count >= 2 else LANG_SW


def has_red_flags(text: str, lang: str) -> bool:
    text_lower = text.lower()
    flags = RED_FLAG_WORDS_SW if lang == LANG_SW else RED_FLAG_WORDS_EN
    return any(f in text_lower for f in flags)


def parse(sms_text: str) -> dict:
    lang = detect_language(sms_text)

    if has_red_flags(sms_text, lang):
        return {
            "lang": lang,
            "disease": None,
            "is_emergency": True,
            "use_ai": False,
            "response": EMERGENCY_SW if lang == LANG_SW else EMERGENCY_EN,
        }

    disease = classify_sms_keywords(sms_text)

    return {
        "lang": lang,
        "disease": disease,
        "is_emergency": False,
        "use_ai": True,
        "response": None,
    }
