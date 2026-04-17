"""
AfyaMkononi SMS Parser v3.0
Intelligent parsing - conversational, no apologies, direct responses.
"""

from services.health_data import classify_sms_keywords
from core.constants import LANG_SW, LANG_EN

# =============================================================================
# EMERGENCY DETECTION - Life-threatening situations
# =============================================================================

RED_FLAG_PHRASES_SW = [
    "hana fahamu", "amepoteza fahamu", "hapumui", "hawezi kupumua",
    "degedege", "mshtuko", "ameanguka", "damu nyingi", 
    "amezimia", "haonyeshi dalili", "amefariki", "kufa",
    "kifafa", "hawezi kuamka", "ganzi mwili wote",
    "hospitali haraka", "dharura", "msaada haraka"
]

RED_FLAG_PHRASES_EN = [
    "unconscious", "not breathing", "cant breathe", "cannot breathe",
    "seizure", "convulsion", "heavy bleeding", "collapsed", "fainted",
    "not responding", "dying", "passed out", "severe bleeding",
    "heart attack", "stroke", "cant wake up", "emergency", "urgent"
]

# =============================================================================
# GREETING DETECTION - Simple and Warm
# =============================================================================

GREETINGS_SW = [
    "habari", "mambo", "vipi", "salama", "shikamoo", "hujambo",
    "niaje", "sema", "poa", "safi", "nzuri", "za leo", "halo",
    "jambo", "ongea", "hello", "hi"
]

GREETINGS_EN = [
    "hi", "hello", "hey", "good morning", "good afternoon", "good evening", 
    "how are you", "whats up", "sup", "yo", "hii", "helo", "greetings"
]

# =============================================================================
# LANGUAGE DETECTION
# =============================================================================

STRONG_EN_MARKERS = [
    "i have", "i am", "i feel", "my child", "my baby", "feeling",
    "help me", "please help", "what is", "how do", "can you",
    "headache", "stomach", "fever", "cough", "pain", "sick",
    "doctor", "hospital", "clinic", "medicine", "treatment",
    "the", "and", "but", "with", "for", "this", "that", "when"
]

STRONG_SW_MARKERS = [
    "nina", "mimi", "mtoto wangu", "mwanangu", "naomba",
    "nisaidie", "nini", "vipi", "kwa nini", "je", "hii",
    "homa", "kichwa", "tumbo", "maumivu", "kikohozi", "kuhara",
    "daktari", "hospitali", "zahanati", "dawa", "tiba",
    "na", "ya", "wa", "kwa", "ni", "au", "lakini", "sana",
    "lini", "wapi", "chanzo", "ilianza"
]

# =============================================================================
# RESPONSE TEMPLATES - Direct, No Apologies
# =============================================================================

EMERGENCY_SW = """Hii ni DHARURA! Dalili hizi ni hatari sana.

Fika HOSPITALI SASA au omba mtu akupeleke haraka. Kila dakika ni muhimu - usisubiri!"""

EMERGENCY_EN = """This is an EMERGENCY! These symptoms are very dangerous.

Get to HOSPITAL NOW or ask someone to take you quickly. Every minute matters - don't wait!"""

GREETING_SW = "Habari! Mimi ni AfyaMkononi. Nikuasaidie nini leo? Niambie unavyojisikia."

GREETING_EN = "Hi! I'm AfyaMkononi. How can I help you today? Tell me how you're feeling."

HELP_SW = """AfyaMkononi - Msaada wa Afya

Niambie dalili zako au unavyojisikia. Mfano:
- "Nina homa na kichwa"
- "Mtoto anakohoa"
- "Kizunguzungu"

Nitakusaidia!"""

HELP_EN = """AfyaMkononi - Health Help

Tell me your symptoms or how you're feeling. Example:
- "I have fever and headache"
- "My child is coughing"
- "I feel dizzy"

I'll help you!"""


def detect_language(text: str) -> str:
    """Detect language based on word markers."""
    text_lower = text.lower()
    
    en_count = sum(1 for phrase in STRONG_EN_MARKERS if phrase in text_lower)
    sw_count = sum(1 for phrase in STRONG_SW_MARKERS if phrase in text_lower)
    
    english_patterns = ["i ", "i'm", "my ", "is ", "are ", "the ", "have ", "feel "]
    en_pattern_count = sum(1 for p in english_patterns if p in text_lower)
    
    swahili_patterns = ["nina", "mimi", "wangu", "yangu", "kwa ", "na ", "ya "]
    sw_pattern_count = sum(1 for p in swahili_patterns if p in text_lower)
    
    total_en = en_count + en_pattern_count
    total_sw = sw_count + sw_pattern_count
    
    if total_en > total_sw:
        return LANG_EN
    
    return LANG_SW


def is_greeting(text: str, lang: str) -> bool:
    """Check if message is a simple greeting."""
    text_lower = text.lower().strip()
    words = text_lower.split()
    
    if len(words) <= 3:
        greetings = GREETINGS_SW + GREETINGS_EN
        return any(g in text_lower for g in greetings)
    
    # Check if starts with greeting
    first_word = words[0] if words else ""
    all_greetings = GREETINGS_SW + GREETINGS_EN
    return first_word in all_greetings and len(words) <= 2


def is_help_request(text: str) -> bool:
    """Check if user is asking for help/info."""
    text_lower = text.lower().strip()
    help_words = ["help", "msaada", "info", "taarifa", "how", "what", "nini", "vipi", "menu", "?"]
    
    if len(text_lower) < 15:
        return any(w in text_lower for w in help_words)
    return False


def has_red_flags(text: str) -> bool:
    """Check for TRUE emergency situations."""
    text_lower = text.lower()
    
    for phrase in RED_FLAG_PHRASES_SW:
        if phrase in text_lower:
            return True
    
    for phrase in RED_FLAG_PHRASES_EN:
        if phrase in text_lower:
            return True
    
    return False


def parse(sms_text: str) -> dict:
    """
    Parse incoming SMS and determine response type.
    
    Returns dict with:
    - lang: detected language
    - disease: classified disease category
    - is_emergency: True if genuine emergency
    - is_greeting: True if simple greeting
    - is_help: True if asking about service
    - use_ai: True if should use AI
    - response: pre-set response (if not using AI)
    """
    text = sms_text.strip()
    lang = detect_language(text)

    # 1. Emergency first
    if has_red_flags(text):
        return {
            "lang": lang,
            "disease": None,
            "is_emergency": True,
            "is_greeting": False,
            "is_help": False,
            "use_ai": False,
            "response": EMERGENCY_SW if lang == LANG_SW else EMERGENCY_EN,
        }

    # 2. Simple greeting
    if is_greeting(text, lang):
        return {
            "lang": lang,
            "disease": None,
            "is_emergency": False,
            "is_greeting": True,
            "is_help": False,
            "use_ai": False,
            "response": GREETING_SW if lang == LANG_SW else GREETING_EN,
        }

    # 3. Help request
    if is_help_request(text):
        return {
            "lang": lang,
            "disease": None,
            "is_emergency": False,
            "is_greeting": False,
            "is_help": True,
            "use_ai": False,
            "response": HELP_SW if lang == LANG_SW else HELP_EN,
        }

    # 4. Health questions - use AI
    disease = classify_sms_keywords(text)

    return {
        "lang": lang,
        "disease": disease,
        "is_emergency": False,
        "is_greeting": False,
        "is_help": False,
        "use_ai": True,
        "response": None,
    }
