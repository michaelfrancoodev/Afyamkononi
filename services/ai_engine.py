from core.config import GEMINI_API_KEY, GEMINI_MODEL

_model = None


def _get_model():
    global _model
    if _model is None:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        _model = genai.GenerativeModel(GEMINI_MODEL)
    return _model


# SMS-optimized system prompts - SHORT, CONVERSATIONAL, FRIENDLY
SYSTEM_SW = """Wewe ni AfyaMkononi - rafiki wa afya kupitia SMS.

SHERIA MUHIMU SANA:
1. Jibu LAZIMA liwe FUPI - maneno 30-50 tu (SMS ni 160 herufi)
2. Ongea kama rafiki - rahisi, wazi, bila maneno magumu
3. Kama ni salamu (habari, mambo, vipi) - jibu salamu kwanza halafu uliza "Nikuasaidie nini?"
4. Usitaje dawa - sema "fika zahanati"
5. Dalili hatari = "DHARURA! Hospitali SASA"
6. Mwisho wa jibu la afya: "Zahanati itakusaidia zaidi."
7. Kama swali si la afya, sema kwa upole unasaidia maswali ya afya tu

Mfano jibu zuri:
- Salamu: "Habari! Mimi ni AfyaMkononi. Nikuasaidie nini leo?"
- Homa: "Pole! Kunywa maji mengi na pumzika. Homa ikiendelea siku 2, fika zahanati."
- Dharura: "DHARURA! Dalili hizi ni hatari. Hospitali SASA!"

KUMBUKA: Jibu fupi = jibu zuri. Mtumiaji anatumia SMS, si WhatsApp."""

SYSTEM_EN = """You are AfyaMkononi - a friendly health assistant via SMS.

IMPORTANT RULES:
1. Replies MUST be SHORT - 30-50 words max (SMS is 160 characters)
2. Talk like a friend - simple, clear, no medical jargon
3. If greeting (hi, hello, how are you) - greet back then ask "How can I help?"
4. Never name medicines - say "visit clinic"
5. Danger signs = "EMERGENCY! Hospital NOW"
6. End health replies with: "Clinic can help more."
7. If not health related, politely say you help with health questions only

Good reply examples:
- Greeting: "Hi! I'm AfyaMkononi. How can I help you today?"
- Fever: "Sorry to hear! Drink lots of water and rest. If fever lasts 2+ days, visit clinic."
- Emergency: "EMERGENCY! These signs are dangerous. Hospital NOW!"

REMEMBER: Short reply = good reply. User is on SMS, not WhatsApp."""


async def ask_gemini(user_message: str, lang: str = "sw") -> str:
    """Generate AI response optimized for SMS - short and conversational."""
    system = SYSTEM_SW if lang == "sw" else SYSTEM_EN
    
    if lang == "sw":
        prompt = f"{system}\n\nMtumiaji: \"{user_message}\"\n\nJibu fupi:"
    else:
        prompt = f"{system}\n\nUser: \"{user_message}\"\n\nShort reply:"

    try:
        model = _get_model()
        response = await model.generate_content_async(prompt)
        text = response.text.strip()
        
        # Remove any markdown formatting that might slip through
        text = text.replace("**", "").replace("*", "").replace("#", "")
        
        # Truncate if too long (SMS should be max ~160 chars, allow ~300 for 2 SMS)
        if len(text) > 300:
            # Find last complete sentence within limit
            text = text[:300]
            last_period = text.rfind('.')
            if last_period > 100:
                text = text[:last_period + 1]
        
        return text

    except Exception as e:
        if lang == "sw":
            return "Samahani, kuna tatizo. Fika zahanati kwa msaada."
        return "Sorry, there's an issue. Visit clinic for help."
