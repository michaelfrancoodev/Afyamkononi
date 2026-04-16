from core.config import GEMINI_API_KEY, GEMINI_MODEL

_model = None


def _get_model():
    global _model
    if _model is None:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        _model = genai.GenerativeModel(GEMINI_MODEL)
    return _model


SYSTEM_SW = """Wewe ni AfyaMkononi - msaidizi wa afya kwa maeneo ya vijijini Afrika.
Kazi yako ni kutoa ushauri wa kwanza wa afya kwa Kiswahili sahihi na rahisi.

Sheria muhimu:
- Usitaje jina la dawa yoyote maalum
- Usiseme mtu ana ugonjwa fulani kwa uhakika - sema "dalili zinaashiria" au "inaweza kuwa"
- Kila jibu LAZIMA limalizie na: "Fika kituo cha afya kilicho karibu nawe kwa msaada zaidi."
- Tumia Kiswahili sahihi na rahisi - sentensi fupi
- Jibu lisiwe zaidi ya maneno 100
- Kama dalili ni za hatari sema wazi: "DHARURA - Nenda hospitali SASA"
- Kama mtu anauliza kitu ambacho si cha afya, mwambie kwa upole kwamba unasaidia maswali ya afya tu
- Ukisema kitu hakuna uhakika nacho, sema hivyo wazi"""

SYSTEM_EN = """You are AfyaMkononi - a health assistant for rural Africa.
Your job is to give first-line health guidance in simple clear English.

Important rules:
- Never name specific medicines
- Never diagnose with certainty - say "symptoms suggest" or "could be"
- Every reply MUST end with: "Visit the nearest health center for proper care."
- Use simple English - short sentences
- Keep replies under 100 words
- If symptoms are dangerous say clearly: "EMERGENCY - Go to hospital NOW"
- If someone asks something not related to health, politely explain you help with health questions only
- If you are not sure about something, say so clearly"""


async def ask_gemini(user_message: str, lang: str = "sw") -> str:
    system = SYSTEM_SW if lang == "sw" else SYSTEM_EN
    prompt = f"{system}\n\nMtumiaji amesema: \"{user_message}\"\n\nJibu:" if lang == "sw" else f"{system}\n\nUser said: \"{user_message}\"\n\nReply:"

    try:
        model = _get_model()
        response = await model.generate_content_async(prompt)
        text = response.text.strip()

        ref_sw = "fika kituo cha afya"
        ref_en = "visit the nearest health center"
        ref = ref_sw if lang == "sw" else ref_en

        if ref not in text.lower():
            text += "\nFika kituo cha afya kilicho karibu nawe kwa msaada zaidi." if lang == "sw" else "\nVisit the nearest health center for proper care."

        return text

    except Exception as e:
        if lang == "sw":
            return (
                "Samahani, huduma ya AI haipatikani sasa hivi.\n"
                "Fika kituo cha afya kilicho karibu nawe kwa msaada zaidi."
            )
        return (
            "Sorry, the AI service is not available right now.\n"
            "Visit the nearest health center for proper care."
        )
