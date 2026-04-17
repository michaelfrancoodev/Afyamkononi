"""
AfyaMkononi SMS Parser
Intelligent parsing of incoming SMS messages for health guidance.
"""

from services.health_data import classify_sms_keywords
from core.constants import LANG_SW, LANG_EN

# =============================================================================
# EMERGENCY DETECTION - Life-threatening situations
# =============================================================================

# Swahili emergency keywords (specific phrases indicating true emergency)
RED_FLAG_PHRASES_SW = [
    "hana fahamu", "amepoteza fahamu", "hapumui", "hawezi kupumua",
    "degedege", "mshtuko", "ameanguka", "damu nyingi", 
    "amezimia", "haonyeshi dalili", "amefariki", "kufa",
    "kifafa", "hawezi kuamka", "ganzi mwili wote"
]

# English emergency keywords
RED_FLAG_PHRASES_EN = [
    "unconscious", "not breathing", "cant breathe", "cannot breathe",
    "seizure", "convulsion", "heavy bleeding", "collapsed", "fainted",
    "not responding", "dying", "passed out", "severe bleeding",
    "heart attack", "stroke", "cant wake up"
]

# =============================================================================
# GREETING DETECTION
# =============================================================================

GREETINGS_SW = [
    "habari", "mambo", "vipi", "salama", "shikamoo", "hujambo",
    "niaje", "sema", "poa", "safi", "nzuri", "za leo", "halo"
]

GREETINGS_EN = [
    "hi", "hello", "hey", "good morning", "good afternoon", "good evening", 
    "how are you", "whats up", "sup", "yo", "hii", "helo"
]

# =============================================================================
# LANGUAGE DETECTION - Improved accuracy
# =============================================================================

# Strong English indicators (words that clearly indicate English)
STRONG_EN_MARKERS = [
    "i have", "i am", "i feel", "my child", "my baby", "feeling",
    "help me", "please help", "what is", "how do", "can you",
    "headache", "stomach", "fever", "cough", "pain", "sick",
    "doctor", "hospital", "clinic", "medicine", "treatment",
    "the", "and", "but", "with", "for", "this", "that"
]

# Strong Swahili indicators
STRONG_SW_MARKERS = [
    "nina", "nina", "mimi", "mtoto wangu", "mwanangu", "naomba",
    "nisaidie", "nini", "vipi", "kwa nini", "je", "hii",
    "homa", "kichwa", "tumbo", "maumivu", "kikohozi", "kuhara",
    "daktari", "hospitali", "zahanati", "dawa", "tiba",
    "na", "ya", "wa", "kwa", "ni", "au", "lakini", "sana"
]

# Common words that appear in both (ignore for detection)
NEUTRAL_WORDS = ["ok", "sms", "afya", "health"]

# =============================================================================
# RESPONSE TEMPLATES - Compassionate, informative
# =============================================================================

# Emergency response - serious but not panic-inducing
EMERGENCY_SW = """Dalili hizi ni muhimu sana na zinahitaji msaada wa haraka.

Tafadhali fika hospitali SASA au omba mtu akupeleke. Usisubiri - kila dakika ni muhimu.

Mungu akubariki."""

EMERGENCY_EN = """These symptoms are very serious and need urgent attention.

Please get to hospital NOW or ask someone to take you. Don't wait - every minute matters.

Take care."""

# Greeting responses - warm and inviting
GREETING_SW = "Habari! Mimi ni AfyaMkononi, msaidizi wako wa afya. Nikuasaidie nini leo? Niambie unavyojisikia."

GREETING_EN = "Hi there! I'm AfyaMkononi, your health assistant. How can I help you today? Tell me how you're feeling."

# Help/info responses
HELP_SW = """AfyaMkononi - Msaada wa Afya kwa SMS

Niambie unavyojisikia au dalili unazoziona. Mfano:
- "Nina homa na maumivu ya kichwa"
- "Mtoto anakohoa sana"
- "Nahisi kizunguzungu"

Nitakusaidia na ushauri wa kwanza."""

HELP_EN = """AfyaMkononi - Health Help via SMS

Tell me how you're feeling or what symptoms you have. Example:
- "I have fever and headache"
- "My child is coughing a lot"
- "I feel dizzy"

I'll give you first-aid guidance."""


def detect_language(text: str) -> str:
    """
    Detect language based on word markers.
    Returns the language the user wrote in so we respond in the same language.
    """
    text_lower = text.lower()
    
    # Count strong English markers
    en_count = sum(1 for phrase in STRONG_EN_MARKERS if phrase in text_lower)
    
    # Count strong Swahili markers
    sw_count = sum(1 for phrase in STRONG_SW_MARKERS if phrase in text_lower)
    
    # Check for clear English patterns
    english_patterns = ["i ", "i'm", "my ", "is ", "are ", "the ", "have ", "feel "]
    en_pattern_count = sum(1 for p in english_patterns if p in text_lower)
    
    # Check for clear Swahili patterns
    swahili_patterns = ["nina", "mimi", "wangu", "yangu", "kwa ", "na ", "ya "]
    sw_pattern_count = sum(1 for p in swahili_patterns if p in text_lower)
    
    total_en = en_count + en_pattern_count
    total_sw = sw_count + sw_pattern_count
    
    # If clearly more English indicators, return English
    if total_en > total_sw:
        return LANG_EN
    
    # Default to Swahili (most users in Tanzania/Kenya)
    return LANG_SW


def is_greeting(text: str, lang: str) -> bool:
    """Check if message is a simple greeting or hello."""
    text_lower = text.lower().strip()
    words = text_lower.split()
    
    # Very short messages (1-3 words) that are greetings
    if len(words) <= 3:
        greetings = GREETINGS_SW + GREETINGS_EN  # Check both languages
        return any(g in text_lower for g in greetings)
    
    return False


def is_help_request(text: str) -> bool:
    """Check if user is asking for help/info about the service."""
    text_lower = text.lower().strip()
    help_words = ["help", "msaada", "info", "taarifa", "how", "what", "nini", "vipi", "menu"]
    
    if len(text_lower) < 15:
        return any(w in text_lower for w in help_words)
    return False


def has_red_flags(text: str) -> bool:
    """
    Check for TRUE emergency situations.
    Only flags genuine emergencies, not just mentions of symptoms.
    """
    text_lower = text.lower()
    
    # Check Swahili emergency phrases
    for phrase in RED_FLAG_PHRASES_SW:
        if phrase in text_lower:
            return True
    
    # Check English emergency phrases
    for phrase in RED_FLAG_PHRASES_EN:
        if phrase in text_lower:
            return True
    
    return False


def parse(sms_text: str) -> dict:
    """
    Parse incoming SMS and determine how to respond.
    
    Returns dict with:
    - lang: detected language (sw/en) - we respond in same language
    - disease: classified disease category (if identifiable)
    - is_emergency: True if genuine emergency detected
    - is_greeting: True if simple greeting
    - is_help: True if asking about the service
    - use_ai: True if should use AI for response
    - response: pre-set response (if not using AI)
    """
    text = sms_text.strip()
    lang = detect_language(text)

    # 1. Check for TRUE emergency first - highest priority
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

    # 2. Check for simple greeting (habari, hi, hello, etc.)
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

    # 3. Check for help/info request
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

    # 4. For health questions - use AI with context from knowledge base
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
