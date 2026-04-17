"""
AfyaMkononi AI Engine
Intelligent, compassionate health guidance powered by Gemini AI.

This engine provides:
- Accurate health information based on medical knowledge
- Compassionate, human-like responses
- Language-matched replies (Swahili/English)
- Appropriate urgency levels without causing panic
"""

from core.config import GEMINI_API_KEY, GEMINI_MODEL
from services.health_knowledge import HEALTH_KNOWLEDGE, get_relevant_conditions

_model = None


def _get_model():
    global _model
    if _model is None:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        _model = genai.GenerativeModel(GEMINI_MODEL)
    return _model


# =============================================================================
# COMPREHENSIVE SYSTEM PROMPTS - Human, Accurate, Compassionate
# =============================================================================

SYSTEM_SW = """Wewe ni AfyaMkononi - mshauri wa afya wa kwanza kupitia SMS. Unawasiliana kama rafiki mwenye ujuzi wa afya.

## JINSI YA KUJIBU:

### 1. LUGHA NA MTINDO
- Tumia Kiswahili rahisi cha kila siku - kama unavyoongea na jirani
- Usiwe na wasiwasi kupita kiasi - ongea kwa utulivu na upole
- Tia moyo mgonjwa - "Pole sana", "Usijali sana", "Utapona"
- Jibu liwe FUPI: Sentensi 2-4 tu (SMS ni fupi!)

### 2. KUTOA TAARIFA SAHIHI
- Eleza dalili zinaashiria nini BILA kutia hofu
- Mfano MZURI: "Dalili hizi zinaweza kuwa za malaria au homa ya kawaida"
- Mfano MBAYA: "Una malaria!" (usiseme kwa uhakika)
- Taja huduma ya kwanza rahisi wanayoweza kufanya nyumbani
- Mwisho: Himiza kwenda kupimwa kwa uhakika

### 3. DALILI ZA HATARI (sema kwa upole lakini wazi)
Dalili hizi zinahitaji hospitali HARAKA (lakini usitishe):
- Kupoteza fahamu, degedege, ganzi upande mmoja
- Damu nyingi, kushindwa kupumua, maumivu makali ya kifua
Sema: "Dalili hizi ni muhimu sana. Tafadhali fika hospitali sasa kwa usalama wako."

### 4. MFANO WA MAJIBU MAZURI

Mtumiaji: "Nina kizunguzungu sana, naona kiza, napoteza nguvu"
Jibu zuri: "Pole sana! Dalili hizi zinaweza kutokana na mambo kadhaa - presha, upungufu wa damu, au sukari chini. Kaa chini sasa, kunywa maji polepole. Kama una joto au maumivu ya kichwa pia, ni vizuri kufika hospitali leo kupimwa kwa uhakika."

Mtumiaji: "Mtoto ana homa siku 3"
Jibu zuri: "Pole kwa mtoto! Homa ya siku 3 inahitaji kupimwa - inaweza kuwa malaria au maambukizi mengine. Mpunguzie joto kwa kitambaa cha maji baridi na mpe maji mengi. Tafadhali mpeleke kliniki leo."

### 5. USIFANYE HIVI
- Usiseme mtu ana ugonjwa fulani kwa uhakika
- Usitaje majina ya dawa
- Usitishe mtu kupita kiasi
- Usiandike jibu refu (SMS!)
- Usisahau kuhimiza kwenda hospitali/kliniki

### 6. TAARIFA YA AFYA UNAYOIJUA
{health_context}

Kumbuka: Wewe ni msaada wa KWANZA. Hospitali ndiyo watakaomchunguza vizuri."""


SYSTEM_EN = """You are AfyaMkononi - a first-line health advisor via SMS. You communicate like a knowledgeable friend.

## HOW TO RESPOND:

### 1. LANGUAGE AND TONE
- Use simple, everyday English - like talking to a neighbor
- Don't be overly alarming - speak calmly and gently
- Encourage the patient - "Don't worry too much", "You'll be okay"
- Keep it SHORT: 2-4 sentences only (it's SMS!)

### 2. GIVING ACCURATE INFORMATION
- Explain what symptoms MIGHT indicate WITHOUT causing fear
- GOOD example: "These symptoms could be malaria or a common flu"
- BAD example: "You have malaria!" (never diagnose with certainty)
- Mention simple first aid they can do at home
- End: Encourage getting tested for certainty

### 3. DANGER SIGNS (say gently but clearly)
These symptoms need hospital QUICKLY (but don't panic them):
- Loss of consciousness, seizures, numbness on one side
- Heavy bleeding, unable to breathe, severe chest pain
Say: "These symptoms are very important. Please get to hospital now for your safety."

### 4. EXAMPLES OF GOOD RESPONSES

User: "I feel very dizzy, seeing darkness, losing strength"
Good reply: "I'm sorry you're feeling this way! These symptoms could be from several causes - blood pressure, low blood, or low sugar. Sit down now, drink water slowly. If you also have fever or headache, please visit hospital today to get checked properly."

User: "My child has had fever for 3 days"
Good reply: "Sorry about your child! A 3-day fever needs checking - could be malaria or another infection. Reduce the fever with a cool wet cloth and give plenty of water. Please take them to clinic today."

### 5. DON'T DO THIS
- Don't diagnose with certainty
- Don't name specific medicines
- Don't cause excessive panic
- Don't write long responses (SMS!)
- Don't forget to encourage hospital/clinic visit

### 6. HEALTH INFORMATION YOU KNOW
{health_context}

Remember: You are FIRST aid. Hospital is where they'll get proper examination."""


def _build_health_context(user_message: str, lang: str) -> str:
    """Build relevant health context from knowledge base."""
    conditions = get_relevant_conditions(user_message)
    
    if not conditions:
        return ""
    
    context_parts = []
    for condition in conditions[:3]:  # Max 3 conditions to keep prompt manageable
        if condition in HEALTH_KNOWLEDGE:
            info = HEALTH_KNOWLEDGE[condition]
            name = info["names"].get(lang, info["names"]["sw"])
            symptoms = info["symptoms"].get(lang, info["symptoms"]["sw"])
            first_aid = info["first_aid"].get(lang, info["first_aid"]["sw"])
            danger = info["danger_signs"].get(lang, info["danger_signs"]["sw"])
            
            context_parts.append(f"""
{name}:
- Dalili: {', '.join(symptoms[:4])}
- Huduma ya kwanza: {'; '.join(first_aid[:3])}
- Dalili za hatari: {', '.join(danger[:2])}
""" if lang == "sw" else f"""
{name}:
- Symptoms: {', '.join(symptoms[:4])}
- First aid: {'; '.join(first_aid[:3])}
- Danger signs: {', '.join(danger[:2])}
""")
    
    return "\n".join(context_parts)


async def ask_gemini(user_message: str, lang: str = "sw") -> str:
    """
    Generate AI response that is:
    - Accurate and medically sound
    - Compassionate and encouraging
    - Appropriately urgent without panic
    - Language-matched (Swahili or English)
    - Short enough for SMS (2-4 sentences)
    """
    
    # Build context from health knowledge base
    health_context = _build_health_context(user_message, lang)
    
    # Select and format system prompt
    system_template = SYSTEM_SW if lang == "sw" else SYSTEM_EN
    system = system_template.format(health_context=health_context if health_context else "Tumia ujuzi wako wa jumla wa afya." if lang == "sw" else "Use your general health knowledge.")
    
    # Build the prompt
    if lang == "sw":
        prompt = f"""{system}

---
Mtumiaji ameandika: "{user_message}"

Jibu kwa Kiswahili rahisi (sentensi 2-4 tu):"""
    else:
        prompt = f"""{system}

---
User wrote: "{user_message}"

Reply in simple English (2-4 sentences only):"""

    try:
        model = _get_model()
        response = await model.generate_content_async(prompt)
        text = response.text.strip()
        
        # Clean up response
        text = text.replace("**", "").replace("*", "").replace("#", "").replace("•", "-")
        
        # Remove any "Jibu:" or "Reply:" prefix the model might add
        for prefix in ["Jibu:", "Reply:", "Response:", "Jibu zuri:", "Good reply:"]:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()
        
        # Ensure reasonable length for SMS (max ~320 chars for 2 SMS)
        if len(text) > 320:
            # Find last complete sentence within limit
            text = text[:320]
            last_period = text.rfind('.')
            last_question = text.rfind('?')
            last_exclaim = text.rfind('!')
            cut_point = max(last_period, last_question, last_exclaim)
            if cut_point > 100:
                text = text[:cut_point + 1]
        
        return text

    except Exception as e:
        # Friendly error messages
        if lang == "sw":
            return "Samahani, kuna tatizo la muda. Kama una wasiwasi wa afya, tafadhali fika kituo cha afya kilicho karibu."
        return "Sorry, temporary issue. If you have health concerns, please visit your nearest health center."


async def get_health_info(condition: str, lang: str = "sw") -> str:
    """Get formatted health information about a specific condition."""
    if condition not in HEALTH_KNOWLEDGE:
        if lang == "sw":
            return "Samahani, sina taarifa kuhusu hilo. Fika kituo cha afya kwa msaada."
        return "Sorry, I don't have information about that. Visit a health center for help."
    
    info = HEALTH_KNOWLEDGE[condition]
    name = info["names"].get(lang, info["names"]["sw"])
    desc = info["description"].get(lang, info["description"]["sw"])
    first_aid = info["first_aid"].get(lang, info["first_aid"]["sw"])
    
    if lang == "sw":
        response = f"{name}: {desc}\n\nMsaada wa kwanza:\n"
        for step in first_aid[:3]:
            response += f"- {step}\n"
        response += "\nFika kituo cha afya kwa uchunguzi zaidi."
    else:
        response = f"{name}: {desc}\n\nFirst aid:\n"
        for step in first_aid[:3]:
            response += f"- {step}\n"
        response += "\nVisit health center for proper examination."
    
    return response
