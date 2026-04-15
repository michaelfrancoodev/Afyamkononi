from core.config import GEMINI_API_KEY, GEMINI_MODEL

_model = None


def _get_model():
    global _model
    if _model is None:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        _model = genai.GenerativeModel(GEMINI_MODEL)
    return _model


SYSTEM_SW = (
    "Wewe ni AfyaMkononi, msaidizi wa afya kwa vijijini Afrika. "
    "Sheria: 1. Usitoe dawa kwa jina. 2. Sema 'inaweza kuwa' badala ya kutambua kwa uhakika. "
    "3. Maliza kila jibu na: 'Fika kituo cha afya kilicho karibu nawe.' "
    "4. Tumia Kiswahili rahisi, sentensi fupi, chini ya maneno 80. "
    "5. Kama hali ni ya hatari sema: 'DHARURA - Nenda hospitali SASA.'"
)

SYSTEM_EN = (
    "You are AfyaMkononi, a health assistant for rural Africa. "
    "Rules: 1. Never name medicines. 2. Say 'could be' instead of diagnosing. "
    "3. End every reply with: 'Visit the nearest health center.' "
    "4. Use simple English, short sentences, under 80 words. "
    "5. If emergency say: 'EMERGENCY - Go to hospital NOW.'"
)


async def ask_gemini(symptoms: str, lang: str = "sw") -> str:
    system = SYSTEM_SW if lang == "sw" else SYSTEM_EN
    prompt = (
        f"{system}\n\nMtumiaji: \"{symptoms}\"\nUshauri mfupi:"
        if lang == "sw" else
        f"{system}\n\nUser: \"{symptoms}\"\nBrief advice:"
    )
    try:
        model = _get_model()
        response = await model.generate_content_async(prompt)
        text = response.text.strip()
        ref = "Fika kituo cha afya" if lang == "sw" else "Visit the nearest health center"
        if ref.lower() not in text.lower():
            text += "\nFika kituo cha afya kilicho karibu nawe." if lang == "sw" else "\nVisit the nearest health center."
        return text
    except Exception:
        if lang == "sw":
            return "Samahani, huduma ya AI haipatikani.\nFika kituo cha afya kilicho karibu nawe."
        return "Sorry, AI service is unavailable.\nPlease visit the nearest health center."
