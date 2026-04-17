from services.health_data import classify_sms_keywords
from core.constants import LANG_SW, LANG_EN

# Red flag words - EMERGENCY situations
RED_FLAG_WORDS_SW = [
    "fahamu", "kuanguka", "degedege", "mshtuko",
    "kushindwa kupumua", "damu nyingi", "kufa", "hana fahamu",
    "hapumui", "damu", "ajali",
]
RED_FLAG_WORDS_EN = [
    "unconscious", "fainted", "seizure", "convulsion",
    "not breathing", "heavy bleeding", "dying", "collapsed",
    "cant breathe", "accident", "bleeding",
]

# Greeting words to detect casual conversation starters
GREETINGS_SW = [
    "habari", "mambo", "vipi", "salama", "shikamoo", "hujambo",
    "niaje", "sema", "za leo", "nzuri", "poa", "safi",
]
GREETINGS_EN = [
    "hi", "hello", "hey", "good morning", "good evening", 
    "how are you", "whats up", "sup", "yo",
]

# English markers for language detection
EN_MARKERS = [
    "fever", "cough", "pain", "help", "sick", "vomit", "diarrhea", 
    "blood", "headache", "stomach", "doctor", "hospital", "clinic",
    "i have", "i am", "my", "feeling", "hurts", "ache",
    "hello", "hi", "please", "thank", "yes", "no", "the", "is", "are",
]

# Swahili markers
SW_MARKERS = [
    "nina", "mimi", "homa", "kichwa", "tumbo", "kuumwa", "maumivu",
    "daktari", "hospitali", "zahanati", "dalili", "ugonjwa",
    "habari", "asante", "tafadhali", "ndiyo", "hapana", "sana",
    "na", "ya", "wa", "kwa", "ni", "au",
]

# Short responses for common situations
EMERGENCY_SW = "DHARURA! Dalili hizi ni hatari. Hospitali SASA! Usisubiri."
EMERGENCY_EN = "EMERGENCY! These signs are dangerous. Hospital NOW! Don't wait."

GREETING_SW = "Habari! Mimi ni AfyaMkononi. Nikuasaidie nini leo?"
GREETING_EN = "Hi! I'm AfyaMkononi. How can I help you today?"


def detect_language(text: str) -> str:
    """Detect language based on word markers - improved accuracy."""
    text_lower = text.lower()
    
    # Count English markers
    en_count = sum(1 for w in EN_MARKERS if w in text_lower)
    
    # Count Swahili markers
    sw_count = sum(1 for w in SW_MARKERS if w in text_lower)
    
    # If clearly more English, return English
    if en_count > sw_count + 1:
        return LANG_EN
    
    # Default to Swahili (most users in Tanzania/Kenya)
    return LANG_SW


def is_greeting(text: str, lang: str) -> bool:
    """Check if message is a simple greeting."""
    text_lower = text.lower().strip()
    
    # Very short messages with greeting words
    greetings = GREETINGS_SW if lang == LANG_SW else GREETINGS_EN
    
    # Check if it's just a greeting (short message)
    if len(text_lower) < 20:
        return any(g in text_lower for g in greetings)
    
    return False


def has_red_flags(text: str, lang: str) -> bool:
    """Check for emergency/danger keywords."""
    text_lower = text.lower()
    flags = RED_FLAG_WORDS_SW if lang == LANG_SW else RED_FLAG_WORDS_EN
    return any(f in text_lower for f in flags)


def parse(sms_text: str) -> dict:
    """Parse SMS and determine response type.
    
    Returns dict with:
    - lang: detected language
    - disease: classified disease (if any)
    - is_emergency: True if red flags detected
    - is_greeting: True if simple greeting
    - use_ai: True if should use AI for response
    - response: pre-set response (if not using AI)
    """
    lang = detect_language(sms_text)

    # Check for emergency first - highest priority
    if has_red_flags(sms_text, lang):
        return {
            "lang": lang,
            "disease": None,
            "is_emergency": True,
            "is_greeting": False,
            "use_ai": False,
            "response": EMERGENCY_SW if lang == LANG_SW else EMERGENCY_EN,
        }

    # Check for simple greeting
    if is_greeting(sms_text, lang):
        return {
            "lang": lang,
            "disease": None,
            "is_emergency": False,
            "is_greeting": True,
            "use_ai": False,
            "response": GREETING_SW if lang == LANG_SW else GREETING_EN,
        }

    # Classify disease keywords for context
    disease = classify_sms_keywords(sms_text)

    # Use AI for health questions
    return {
        "lang": lang,
        "disease": disease,
        "is_emergency": False,
        "is_greeting": False,
        "use_ai": True,
        "response": None,
    }
