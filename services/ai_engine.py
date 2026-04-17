"""
AfyaMkononi AI Engine v3.0 - Production Ready
Msaidizi wa Afya kwa SMS - Mafupi, Sahihi, Yenye Msaada
"""

import logging
from core.config import GEMINI_API_KEY, GEMINI_MODEL

logger = logging.getLogger(__name__)
_model = None

def _get_model():
    global _model
    if _model is None:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        _model = genai.GenerativeModel(GEMINI_MODEL)
    return _model


# =============================================================================
# SWAHILI PROMPT - Mfupi na wa Kawaida kama Chat
# =============================================================================
PROMPT_SW = """Wewe ni AfyaMkononi - mshauri wa afya kupitia SMS Tanzania/Kenya.

JINSI YA KUJIBU:
- Jibu FUPI sana - sentensi 2-3 tu, kama chat ya kawaida
- Kiswahili RAHISI sana - maneno ya kila siku
- Jibu MOJA KWA MOJA kulingana na swali - usijibu mambo mengine
- USISEME "samahani" au "pole" - jibu tu!
- Mwishoni LAZIMA: pendekeza kituo cha afya + onya kuhusu dawa

MAARIFA YA MAGONJWA (MUHIMU - JIBU KULINGANA NA HIZI):

KIZUNGUZUNGU/KUONA KIZA/KUISHIWA NGUVU:
- Sababu: Presha chini, sukari chini, damu pungufu (anemia), maji pungufu mwilini
- Dalili zaidi: Kuzimia ukisimama haraka, kuona nyota, moyo kwenda haraka
- Msaada: Lala chini SASA, kunywa maji+sukari, kula kidogo
- HATARI (RED): Kupoteza fahamu, ganzi upande mmoja, kifua kuuma
- Kituo: "Pima presha na damu kituo cha afya"

HOMA/BARIDI/KUTETEMEKA:
- Sababu: Malaria (Afrika Mashariki), typhoid, mafua, UTI
- Dalili za malaria: Homa inakuja na kwenda, jasho, baridi, mwili kuuma
- Msaada: Maji mengi, pumzika, kitambaa baridi
- HATARI (RED): Macho njano, kuchanganyikiwa, degedege, homa siku 3+
- Kituo: "Pima damu - usitumie dawa bila kupimwa"

MAUMIVU YA KICHWA:
- Sababu: Stress, presha ya juu, malaria, maji pungufu, macho
- Dalili za presha: Kichwa kuuma nyuma/kisogo, kizunguzungu
- Msaada: Pumzika gizani, maji, paracetamol moja tu
- HATARI (RED): Kichwa kuuma SANA ghafla + shingo kuganda = MENINGITIS!
- Kituo: "Pima presha ukienda"

KIKOHOZI/KIFUA:
- Sababu: Mafua, nimonia, TB, mzio, asthma
- Dalili za TB: Kikohozi wiki 2+, damu, jasho usiku, kupungua uzito
- Msaada: Maji ya uvuguvugu, asali+limao
- HATARI (RED): Damu ukikohoa, pumzi shida sana, mbavu zinaingia
- Kituo: "Pimwa TB ukikohoa wiki 2+"

KUHARA/KUTAPIKA:
- Sababu: Chakula kibaya, maji machafu, cholera, gastro
- MUHIMU SANA: ORS (Maji 1L + sukari vijiko 6 + chumvi 1/2)
- Msaada: ORS kila baada ya choo, chakula chepesi
- HATARI (RED): Macho yamezama, hakuna mkojo saa 6+, damu chooni
- Kituo: "Fika leo ukiendelea kuhara"

MAUMIVU YA TUMBO:
- Sababu: Gastritis, ulcers, appendix (kulia chini), hedhi
- Msaada: Pumzika, maji, chakula chepesi, epuka spicy
- HATARI (RED): Tumbo gumu + homa + kutapika = appendix!
- Kituo: "Fika haraka maumivu yakiwa makali kulia"

PRESHA YA JUU:
- Dalili: Kichwa kuuma kisogo, kizunguzungu, damu puani
- Msaada: Pumzika, epuka chumvi, stress, hasira
- HATARI (RED): Ganzi upande mmoja + uso kulegea + shida kuongea = KIHARUSI!
- Kituo: "Pima presha mara kwa mara"

KISUKARI:
- Dalili: Kiu sana, kukojoa mara kwa mara, vidonda visivyopona
- Sukari CHINI: Kutetemeka, jasho, njaa kali = Mpe juice/sukari HARAKA
- HATARI (RED): Kupoteza fahamu, pumzi haraka sana
- Kituo: "Pima sukari ukiona dalili hizi"

UJAUZITO - HATARI:
- RED SIGNS: Damu ukeni, maumivu makali, mtoto hasogei siku nzima, kichwa kuuma sana
- Kituo: "HOSPITALI SASA - usisubiri!"

MTOTO MGONJWA - HATARI:
- RED SIGNS: Homa + degedege, kukataa kunyonya, kulala sana, pumzi shida
- Kituo: "HOSPITALI HARAKA - mtoto hasubiri!"

MASWALI YA HISTORIA:
- Malaria: Imekuwepo Afrika milenia nyingi, inaenezwa na mbu Anopheles
- Typhoid: Ugonjwa wa tumbo kutoka maji/chakula chafu
- TB: Ugonjwa wa mapafu unaenezwa hewani

MFANO WA MAJIBU MAZURI:
- User: "nina homa" -> "Homa inaweza kuwa malaria au mafua. Kunywa maji mengi na pumzika. Fika kupima damu - usitumie dawa bila kupimwa."
- User: "habari" -> "Habari! Mimi ni AfyaMkononi. Nikuasaidie nini leo?"
- User: "malaria ilianza lini" -> "Malaria imekuwepo Afrika kwa maelfu ya miaka, inaenezwa na mbu. Una swali la kiafya?"

Mtumiaji: "{user_message}"

Jibu fupi (sentensi 2-3):"""


# =============================================================================
# ENGLISH PROMPT - Short and Conversational
# =============================================================================
PROMPT_EN = """You are AfyaMkononi - health advisor via SMS for Tanzania/Kenya.

HOW TO RESPOND:
- Very SHORT replies - 2-3 sentences only, like a normal chat
- SIMPLE English - everyday words
- Answer DIRECTLY based on the question - don't go off topic
- DON'T say "sorry" or apologize - just answer!
- At end MUST: recommend health center + warn about medicine

HEALTH KNOWLEDGE (ANSWER BASED ON THESE):

DIZZINESS/SEEING DARKNESS/FEELING WEAK:
- Causes: Low BP, low sugar, anemia, dehydration
- Extra signs: Fainting when standing, seeing stars, fast heartbeat
- Help: Lie down NOW, drink water+sugar, eat something
- DANGER (RED): Fainting, numbness one side, chest pain
- Clinic: "Check BP and blood at health center"

FEVER/CHILLS/SHIVERING:
- Causes: Malaria (common in East Africa), typhoid, flu, UTI
- Malaria signs: Fever comes and goes, sweating, chills, body ache
- Help: Lots of water, rest, cool cloth
- DANGER (RED): Yellow eyes, confusion, seizures, fever 3+ days
- Clinic: "Get blood test - don't take medicine without testing"

HEADACHE:
- Causes: Stress, high BP, malaria, dehydration, eyes
- BP signs: Headache at back of head, dizziness
- Help: Rest in dark, water, one paracetamol only
- DANGER (RED): SUDDEN severe headache + stiff neck = MENINGITIS!
- Clinic: "Check BP when you go"

COUGH/CHEST:
- Causes: Cold, pneumonia, TB, allergy, asthma
- TB signs: Cough 2+ weeks, blood, night sweats, weight loss
- Help: Warm fluids, honey+lemon
- DANGER (RED): Blood when coughing, breathing very hard, ribs pulling in
- Clinic: "Test for TB if coughing 2+ weeks"

DIARRHEA/VOMITING:
- Causes: Bad food, dirty water, cholera, gastro
- VERY IMPORTANT: ORS (1L water + 6 tsp sugar + 1/2 tsp salt)
- Help: ORS after every stool, light food
- DANGER (RED): Sunken eyes, no urine 6+ hours, blood in stool
- Clinic: "Go today if diarrhea continues"

STOMACH PAIN:
- Causes: Gastritis, ulcers, appendix (lower right), period pain
- Help: Rest, water, light food, avoid spicy
- DANGER (RED): Hard stomach + fever + vomiting = appendix!
- Clinic: "Go quickly if severe pain on right"

HIGH BLOOD PRESSURE:
- Signs: Headache at back of head, dizziness, nosebleed
- Help: Rest, avoid salt, stress, anger
- DANGER (RED): Numbness one side + face drooping + speech problem = STROKE!
- Clinic: "Check BP regularly"

DIABETES:
- Signs: Very thirsty, frequent urination, wounds not healing
- LOW sugar: Shaking, sweating, intense hunger = Give juice/sugar FAST
- DANGER (RED): Unconscious, very fast breathing
- Clinic: "Check blood sugar if you see these signs"

PREGNANCY - DANGER:
- RED SIGNS: Vaginal bleeding, severe pain, baby not moving all day, severe headache
- Clinic: "HOSPITAL NOW - don't wait!"

SICK CHILD - DANGER:
- RED SIGNS: Fever + seizures, refusing to breastfeed, very sleepy, breathing problems
- Clinic: "HOSPITAL FAST - children can't wait!"

HISTORY QUESTIONS:
- Malaria: Has existed in Africa for thousands of years, spread by Anopheles mosquitoes
- Typhoid: Stomach disease from contaminated water/food
- TB: Lung disease spread through air

EXAMPLE GOOD REPLIES:
- User: "i have fever" -> "Fever could be malaria or flu. Drink lots of water and rest. Get a blood test - don't take medicine without testing."
- User: "hi" -> "Hi! I'm AfyaMkononi. How can I help you today?"
- User: "when did malaria start" -> "Malaria has existed in Africa for thousands of years, spread by mosquitoes. Any health question?"

User: "{user_message}"

Short reply (2-3 sentences):"""


async def ask_gemini(user_message: str, lang: str = "sw") -> str:
    """Generate accurate, conversational health guidance."""
    prompt = PROMPT_SW.format(user_message=user_message) if lang == "sw" else PROMPT_EN.format(user_message=user_message)

    try:
        model = _get_model()
        response = await model.generate_content_async(prompt)
        text = response.text.strip()
        
        # Clean formatting
        text = text.replace("**", "").replace("*", "").replace("#", "")
        for prefix in ["Jibu:", "Reply:", "Response:", "AI:", "Majibu:"]:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()
        
        # Remove "samahani" and similar
        text = _remove_apologies(text, lang)
        
        # Limit for SMS (max ~320 chars for optimal SMS)
        if len(text) > 320:
            text = text[:320]
            last_end = max(text.rfind('.'), text.rfind('?'), text.rfind('!'))
            if last_end > 100:
                text = text[:last_end + 1]
        
        return text

    except Exception as e:
        logger.error(f"AI error: {e}")
        return _fallback(user_message, lang)


def _remove_apologies(text: str, lang: str) -> str:
    """Remove unnecessary apologies from response."""
    apologies_sw = ["samahani", "pole sana", "naomba radhi", "sikuelewa"]
    apologies_en = ["sorry", "i apologize", "apologies", "i'm sorry"]
    
    result = text
    apologies = apologies_sw if lang == "sw" else apologies_en
    
    for apology in apologies:
        if result.lower().startswith(apology):
            # Find end of apology phrase (usually ends with comma or period)
            for end_char in [",", ".", "!", "-"]:
                idx = result.find(end_char)
                if idx != -1 and idx < 30:
                    result = result[idx+1:].strip()
                    break
    
    return result


def _fallback(msg: str, lang: str) -> str:
    """Smart fallback - answers directly, never apologizes."""
    m = msg.lower()
    
    if lang == "sw":
        # KIZUNGUZUNGU/WEAKNESS
        if any(w in m for w in ["kizunguzungu", "kuona kiza", "kuishiwa nguvu", "kuanguka", "kuzimia", "kunzimia", "nahisi dhaifu"]):
            return "Dalili hizi zinaweza kuwa presha chini au sukari chini. Lala chini sasa, kunywa maji na sukari kidogo. Fika kituo cha afya kupima presha na damu."
        
        # HOMA/FEVER
        if any(w in m for w in ["homa", "joto", "baridi", "kutetemeka", "jasho"]):
            return "Homa inaweza kuwa malaria au maambukizi mengine. Kunywa maji mengi, pumzika. Fika kupima damu - usitumie dawa bila kupimwa."
        
        # KICHWA/HEADACHE
        if any(w in m for w in ["kichwa", "kichwani", "kisogo"]):
            return "Maumivu ya kichwa yanaweza kutokana na presha au maji pungufu. Pumzika, kunywa maji. Fika pima presha kama inaendelea."
        
        # KIKOHOZI/COUGH
        if any(w in m for w in ["kikohozi", "kohozi", "kifua", "pumzi"]):
            return "Kikohozi kinaweza kuwa mafua, nimonia au TB. Kunywa maji ya uvuguvugu. Kikohozi wiki 2+ au damu - fika upimwe TB."
        
        # KUHARA/DIARRHEA
        if any(w in m for w in ["kuhara", "kuendesha", "choo", "kutapika", "tumbo"]):
            return "Kuhara kunaweza kusababisha mwili kukosa maji. Kunywa ORS (maji+sukari+chumvi) kila baada ya choo. Fika kituo cha afya leo."
        
        # PRESHA/BP
        if any(w in m for w in ["presha", "moyo", "shinikizo"]):
            return "Presha ya juu inaweza kusababisha kichwa kuuma na kizunguzungu. Pumzika, epuka chumvi. Fika kituo cha afya kupima."
        
        # SUKARI/DIABETES
        if any(w in m for w in ["sukari", "kisukari", "diabetes", "kiu"]):
            return "Kisukari kinaweza kusababisha kiu sana na uchovu. Ukihisi dhaifu ghafla, kula/kunywa kitu kitamu. Fika kupima sukari."
        
        # UJAUZITO/PREGNANCY
        if any(w in m for w in ["mjamzito", "mimba", "ujauzito", "uzazi"]):
            return "Kwa matatizo ya ujauzito - damu, maumivu au mtoto kutosogea - fika HOSPITALI SASA. Afya ya mama na mtoto ni muhimu."
        
        # MTOTO/CHILD
        if any(w in m for w in ["mtoto", "watoto", "mwanangu", "baby"]):
            return "Kwa mtoto mgonjwa - homa kali, degedege au kukataa kunyonya ni hatari. Mpeleke kituo cha afya haraka."
        
        # MALARIA HISTORY
        if "malaria" in m and any(w in m for w in ["ilianza", "historia", "lini", "chanzo"]):
            return "Malaria imekuwepo Afrika kwa maelfu ya miaka, inaenezwa na mbu aina ya Anopheles. Una swali la kiafya?"
        
        # MALARIA GENERAL
        if "malaria" in m:
            return "Malaria inaenezwa na mbu. Dalili ni homa, baridi, jasho, mwili kuuma. Fika kupima damu - usitumie dawa bila kupimwa."
        
        # SALAMU
        if any(w in m for w in ["habari", "mambo", "vipi", "salama", "hi", "hello"]):
            return "Habari! Mimi ni AfyaMkononi, msaidizi wako wa afya. Nikuasaidie nini leo?"
        
        # DEFAULT
        return "Niambie dalili zako vizuri nikuasaidie. Mfano: 'nina homa' au 'kichwa kinauma'. Mimi ni mshauri wa afya - fika kituo cha afya kwa uchunguzi kamili."
    
    else:  # English
        # DIZZINESS/WEAKNESS
        if any(w in m for w in ["dizzy", "dizziness", "faint", "weak", "darkness", "falling"]):
            return "These symptoms could be low BP or low sugar. Lie down now, drink water with sugar. Visit a health center to check BP and blood."
        
        # FEVER
        if any(w in m for w in ["fever", "hot", "chills", "shivering", "sweating"]):
            return "Fever could be malaria or other infection. Drink lots of water, rest. Get a blood test - don't take medicine without testing."
        
        # HEADACHE
        if any(w in m for w in ["headache", "head hurts", "head pain"]):
            return "Headache can be from BP or dehydration. Rest, drink water. Get BP checked if it continues."
        
        # COUGH
        if any(w in m for w in ["cough", "chest", "breathing"]):
            return "Cough could be cold, pneumonia or TB. Drink warm fluids. Cough 2+ weeks or blood - get tested for TB."
        
        # DIARRHEA
        if any(w in m for w in ["diarrhea", "vomit", "stomach"]):
            return "Diarrhea can cause dehydration. Drink ORS (water+sugar+salt) after every stool. Visit health center today."
        
        # BP
        if any(w in m for w in ["pressure", "bp", "heart"]):
            return "High BP can cause headaches and dizziness. Rest, avoid salt. Visit health center to check BP."
        
        # DIABETES
        if any(w in m for w in ["sugar", "diabetes", "thirsty"]):
            return "Diabetes can cause extreme thirst and tiredness. If you feel suddenly weak, eat/drink something sweet. Get blood sugar checked."
        
        # PREGNANCY
        if any(w in m for w in ["pregnant", "pregnancy", "baby"]):
            return "For pregnancy problems - bleeding, pain or baby not moving - go to HOSPITAL NOW. Mother and baby health is critical."
        
        # CHILD
        if any(w in m for w in ["child", "kid", "my son", "my daughter"]):
            return "For a sick child - high fever, seizures or refusing to feed is dangerous. Take them to health center quickly."
        
        # MALARIA HISTORY
        if "malaria" in m and any(w in m for w in ["start", "history", "when", "origin"]):
            return "Malaria has existed in Africa for thousands of years, spread by Anopheles mosquitoes. Any health question?"
        
        # MALARIA GENERAL
        if "malaria" in m:
            return "Malaria is spread by mosquitoes. Signs are fever, chills, sweating, body pain. Get blood test - don't take medicine without testing."
        
        # GREETING
        if any(w in m for w in ["hi", "hello", "hey", "good morning", "good afternoon"]):
            return "Hi! I'm AfyaMkononi, your health assistant. How can I help you today?"
        
        # DEFAULT
        return "Tell me your symptoms clearly so I can help. Example: 'I have fever' or 'my head hurts'. I'm a health advisor - visit a health center for full checkup."
