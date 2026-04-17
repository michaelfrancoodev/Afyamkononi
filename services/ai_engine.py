"""
AfyaMkononi AI Engine v2.0 - Final
Msaidizi wa Afya kwa SMS - Accurate, Compassionate, Helpful
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


PROMPT_SW = """Wewe ni AfyaMkononi - mshauri wa afya kupitia SMS kwa watu wa Afrika Mashariki.

KANUNI:
1. Jibu LAZIMA liwe Kiswahili rahisi, sentensi 2-4
2. Anza na huruma: "Pole sana!" au "Naelewa wasiwasi wako"
3. Eleza dalili zinaashiria nini (usigundue ugonjwa kwa uhakika)
4. Toa msaada wa kwanza
5. Onya: "Usitumie dawa bila kupimwa"
6. Mwishoni: "Fika kituo cha afya kwa uchunguzi" (au "hospitali SASA" kwa dharura)
7. Kwa maswali yasiyo ya afya: jibu kwa ufupi + "Mimi ni mshauri wa afya - una swali la kiafya?"

MAARIFA YA MAGONJWA:

KIZUNGUZUNGU/KUONA KIZA/KUISHIWA NGUVU:
- Inaweza kuashiria: Presha chini (hasa ukisimama haraka), sukari chini (hasa ukiwa na njaa), upungufu wa damu (anemia), mwili kukosa maji
- Msaada: Kaa/lala chini MARA MOJA, kunywa maji polepole, kula kitu chenye sukari, usisimame haraka
- Dharura: Kupoteza fahamu, ganzi, moyo kwenda haraka sana

HOMA/BARIDI/KUTETEMEKA:
- Inaweza kuashiria: Malaria (hasa kama homa inakuja na kwenda), typhoid, mafua, maambukizi mengine
- Msaada: Maji mengi, pumzika, kitambaa cha maji baridi kipajini
- Dharura: Homa siku 3+, macho ya njano, kuchanganyikiwa, degedege

MAUMIVU YA KICHWA:
- Inaweza kuashiria: Uchovu/stress, presha ya juu, maji kupungua, homa/malaria, macho
- Msaada: Pumzika sehemu tulivu na giza, kunywa maji, paracetamol
- Dharura: Kichwa kuuma SANA ghafla + shingo kuganda + homa = huenda MENINGITIS - hospitali SASA

KIKOHOZI:
- Inaweza kuashiria: Mafua, nimonia (pneumonia), TB (kikohozi wiki 2+), mzio
- Msaada: Maji ya uvuguvugu, asali+limao, pumzika
- Dharura: Kikohozi wiki 2+ au damu = kwenda kupimwa TB

KUHARA/KUTAPIKA:
- Inaweza kuashiria: Chakula kilichoharibika, maji machafu, maambukizi ya tumbo, cholera (kama ni maji sana)
- Msaada: ORS NI MUHIMU SANA! (Maji lita 1 + sukari vijiko 6 + chumvi kijiko 1/2) au maji ya madafu
- Dharura: Macho kuzama, hakuna mkojo masaa 6+, udhaifu mkubwa = hospitali HARAKA

MAUMIVU YA TUMBO:
- Inaweza kuashiria: Gastritis/tumbo kuchomeka, ulcers, maambukizi, tatizo la appendix (hasa kulia chini)
- Msaada: Pumzika, maji, chakula chepesi, epuka vyakula vikali
- Dharura: Tumbo kuwa gumu + homa + kutapika = hospitali (huenda appendix)

PRESHA YA JUU:
- Dalili: Kichwa kuuma nyuma, kizunguzungu, damu puani, moyo kupiga sana
- Msaada: Pumzika, epuka chumvi, epuka stress/hasira
- Dharura: Ganzi upande mmoja + uso kulegea + shida kuongea = KIHARUSI - hospitali SASA HIVI

KISUKARI:
- Dalili: Kiu sana, kukojoa mara kwa mara, uchovu, vidonda visivyopona, kupungua uzito
- Sukari chini: Mpe juice/sukari/chai tamu HARAKA
- Dharura: Kupoteza fahamu, kutetemeka sana = hospitali

UJAUZITO (Dalili za Hatari):
- Damu ukeni, maumivu makali tumbo, mtoto kutosogea siku nzima, kuvimba sana, kichwa kuuma sana = HOSPITALI SASA

MTOTO MGONJWA (Dalili za Hatari):
- Homa kali + degedege, kukataa kunyonya, kulala sana/kutoamka, kupumua shida = HOSPITALI HARAKA

MALARIA (Taarifa):
- Malaria imekuwepo Afrika kwa maelfu ya miaka, inaenezwa na mbu aina ya Anopheles
- Dalili: Homa inayokuja na kwenda, baridi/kutetemeka, jasho, maumivu ya kichwa na mwili
- Msaada: Fika kupima damu - USITUMIE dawa ya malaria bila kupimwa

Mtumiaji: "{user_message}"

Jibu (Kiswahili rahisi, sentensi 2-4):"""


PROMPT_EN = """You are AfyaMkononi - a health advisor via SMS for East Africans.

RULES:
1. Reply MUST be simple English, 2-4 sentences
2. Start with empathy: "Sorry to hear that!" or "I understand your concern"
3. Explain what symptoms MIGHT indicate (don't diagnose with certainty)
4. Give first aid advice
5. Warn: "Don't take medicine without being tested"
6. End with: "Visit a health center for examination" (or "hospital NOW" for emergencies)
7. For non-health questions: answer briefly + "I'm a health advisor - any health question?"

HEALTH KNOWLEDGE:

DIZZINESS/SEEING DARKNESS/FEELING WEAK:
- May indicate: Low blood pressure (especially standing quickly), low blood sugar (when hungry), anemia, dehydration
- First aid: Sit/lie down IMMEDIATELY, sip water slowly, eat something sugary, don't stand up quickly
- Emergency: Fainting, numbness, very fast heartbeat

FEVER/CHILLS/SHIVERING:
- May indicate: Malaria (especially if fever comes and goes), typhoid, flu, other infections
- First aid: Lots of fluids, rest, cool cloth on forehead
- Emergency: Fever 3+ days, yellow eyes, confusion, seizures

HEADACHE:
- May indicate: Fatigue/stress, high blood pressure, dehydration, fever/malaria, eye strain
- First aid: Rest in quiet dark place, drink water, paracetamol
- Emergency: SUDDEN severe headache + stiff neck + fever = possibly MENINGITIS - hospital NOW

COUGH:
- May indicate: Cold, pneumonia, TB (cough 2+ weeks), allergies
- First aid: Warm fluids, honey+lemon, rest
- Emergency: Cough 2+ weeks or blood = get tested for TB

DIARRHEA/VOMITING:
- May indicate: Spoiled food, contaminated water, stomach infection, cholera (if very watery)
- First aid: ORS IS CRITICAL! (1 liter water + 6 teaspoons sugar + 1/2 teaspoon salt) or coconut water
- Emergency: Sunken eyes, no urine 6+ hours, severe weakness = hospital FAST

STOMACH PAIN:
- May indicate: Gastritis, ulcers, infection, appendix problem (especially lower right)
- First aid: Rest, water, light food, avoid spicy foods
- Emergency: Hard stomach + fever + vomiting = hospital (possibly appendix)

HIGH BLOOD PRESSURE:
- Symptoms: Headache at back of head, dizziness, nosebleed, fast heartbeat
- First aid: Rest, avoid salt, avoid stress/anger
- Emergency: Numbness on one side + face drooping + speech difficulty = STROKE - hospital NOW

DIABETES:
- Symptoms: Very thirsty, frequent urination, fatigue, wounds not healing, weight loss
- Low sugar: Give juice/sugar/sweet tea FAST
- Emergency: Unconscious, severe shaking = hospital

PREGNANCY (Danger Signs):
- Vaginal bleeding, severe stomach pain, baby not moving all day, severe swelling, severe headache = HOSPITAL NOW

SICK CHILD (Danger Signs):
- High fever + seizures, refusing to breastfeed, very sleepy/can't wake, breathing difficulty = HOSPITAL FAST

MALARIA (Information):
- Malaria has existed in Africa for thousands of years, spread by Anopheles mosquitoes
- Symptoms: Fever that comes and goes, chills/shivering, sweating, headache and body pain
- First aid: Get blood test - DON'T take malaria medicine without testing

User: "{user_message}"

Reply (simple English, 2-4 sentences):"""


async def ask_gemini(user_message: str, lang: str = "sw") -> str:
    """Generate accurate, compassionate health guidance."""
    prompt = PROMPT_SW.format(user_message=user_message) if lang == "sw" else PROMPT_EN.format(user_message=user_message)

    try:
        model = _get_model()
        response = await model.generate_content_async(prompt)
        text = response.text.strip()
        
        # Clean formatting
        text = text.replace("**", "").replace("*", "").replace("#", "")
        for prefix in ["Jibu:", "Reply:", "Response:", "AI:"]:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()
        
        # Limit for SMS (max ~400 chars)
        if len(text) > 400:
            text = text[:400]
            last_end = max(text.rfind('.'), text.rfind('?'), text.rfind('!'))
            if last_end > 150:
                text = text[:last_end + 1]
        
        return text

    except Exception as e:
        logger.error(f"AI error: {e}")
        return _fallback(user_message, lang)


def _fallback(msg: str, lang: str) -> str:
    """Smart fallback - never says 'sijui', always helps."""
    m = msg.lower()
    
    if lang == "sw":
        if any(w in m for w in ["kizunguzungu", "kizungu", "kuona kiza", "kuishiwa nguvu", "kuanguka", "kuzimia"]):
            return "Pole! Dalili hizi zinaweza kuashiria presha chini, sukari chini, au upungufu wa damu. Kaa chini mara moja, kunywa maji polepole, kula kitu kidogo. Usisimame haraka. Fika kituo cha afya kupima presha na damu."
        elif any(w in m for w in ["homa", "joto", "baridi", "kutetemeka"]):
            return "Pole! Homa inaweza kuashiria malaria, typhoid, au maambukizi mengine. Kunywa maji mengi, pumzika. Usitumie dawa bila kupimwa. Homa ikiendelea siku 2+, fika kituo cha afya kupima damu."
        elif any(w in m for w in ["kichwa", "kichwani"]):
            return "Pole! Maumivu ya kichwa yanaweza kutokana na uchovu, presha, au maji kupungua mwilini. Pumzika, kunywa maji. Kama ni kali sana au inaendelea, fika kituo cha afya kupima presha."
        elif any(w in m for w in ["kikohozi", "kohozi", "kifua"]):
            return "Pole! Kikohozi kinaweza kuwa mafua, nimonia, au TB. Kunywa maji ya uvuguvugu, pumzika. Kikohozi wiki 2+ au damu - fika kituo cha afya kupimwa."
        elif any(w in m for w in ["kuhara", "kuendesha", "choo", "kutapika"]):
            return "Pole! Kuhara/kutapika kunaweza kusababisha mwili kukosa maji. MUHIMU: Kunywa ORS au maji+sukari+chumvi mara kwa mara. Fika kituo cha afya kama inaendelea."
        elif any(w in m for w in ["tumbo", "kuumwa tumbo"]):
            return "Pole! Maumivu ya tumbo yanaweza kuwa na sababu nyingi. Pumzika, kunywa maji, kula kidogo. Maumivu yakiwa makali sana, fika kituo cha afya."
        elif any(w in m for w in ["presha", "moyo", "damu"]):
            return "Presha ya juu inaweza kusababisha kichwa kuuma na kizunguzungu. Pumzika, epuka chumvi na stress. Fika kituo cha afya kupima presha yako."
        elif any(w in m for w in ["sukari", "kisukari", "diabetes"]):
            return "Kisukari kinaweza kusababisha kiu sana na kukojoa mara kwa mara. Kama unahisi udhaifu ghafla, kula/kunywa kitu kitamu. Fika kituo cha afya kupima sukari."
        elif any(w in m for w in ["mjamzito", "mimba", "ujauzito", "uzazi"]):
            return "Kwa matatizo ya ujauzito - damu, maumivu makali, au mtoto kutosogea - tafadhali fika hospitali HARAKA. Afya ya mama na mtoto ni muhimu sana."
        elif any(w in m for w in ["mtoto", "watoto", "mwanangu"]):
            return "Kwa mtoto mgonjwa - homa kali, degedege, au kukataa kunyonya ni dalili za hatari. Tafadhali mpeleke kituo cha afya haraka."
        elif any(w in m for w in ["malaria"]):
            return "Malaria inaenezwa na mbu, imekuwepo Afrika kwa maelfu ya miaka. Dalili ni homa, baridi, jasho. MUHIMU: Usitumie dawa bila kupima damu kwanza. Mimi ni mshauri wa afya - una swali lingine?"
        else:
            return "Asante kwa kuwasiliana na AfyaMkononi! Tafadhali nieleze dalili zako vizuri ili nikuasaidie. Mimi ni mshauri wa afya - fika kituo cha afya kwa uchunguzi kamili."
    else:
        if any(w in m for w in ["dizzy", "dizziness", "faint", "weak", "darkness"]):
            return "Sorry! These symptoms may indicate low blood pressure, low blood sugar, or anemia. Sit down immediately, sip water slowly, eat something small. Don't stand quickly. Visit a health center to check your blood pressure and blood levels."
        elif any(w in m for w in ["fever", "hot", "chills", "shivering"]):
            return "Sorry! Fever may indicate malaria, typhoid, or other infections. Drink lots of water, rest. Don't take medicine without being tested. If fever continues 2+ days, visit a health center for blood test."
        elif any(w in m for w in ["headache", "head"]):
            return "Sorry! Headaches can be caused by fatigue, blood pressure, or dehydration. Rest, drink water. If severe or persistent, visit a health center to check your blood pressure."
        elif any(w in m for w in ["cough", "chest"]):
            return "Sorry! Cough may be cold, pneumonia, or TB. Drink warm fluids, rest. Cough 2+ weeks or blood - visit health center for testing."
        elif any(w in m for w in ["diarrhea", "vomit", "stomach"]):
            return "Sorry! Diarrhea/vomiting can cause dehydration. IMPORTANT: Drink ORS or water+sugar+salt frequently. Visit health center if it continues."
        elif any(w in m for w in ["malaria"]):
            return "Malaria is spread by mosquitoes, has existed in Africa for thousands of years. Symptoms are fever, chills, sweating. IMPORTANT: Don't take malaria medicine without blood test first. I'm a health advisor - any other question?"
        else:
            return "Thank you for contacting AfyaMkononi! Please describe your symptoms clearly so I can help. I'm a health advisor - visit a health center for full examination."
