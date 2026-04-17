"""
AfyaMkononi Health Data v3.0
Comprehensive disease database with severity levels and accurate medical info.
"""

DISEASES = {
    # =========================================================================
    # MALARIA - Common in East Africa
    # =========================================================================
    "malaria": {
        "name_sw": "Malaria",
        "name_en": "Malaria",
        "symptoms_sw": [
            "homa (mwili kuwa moto)",
            "baridi na kutetemeka",
            "jasho baada ya homa",
            "maumivu ya kichwa",
            "maumivu ya mwili na viungo",
            "kichefuchefu au kutapika",
            "uchovu mkubwa"
        ],
        "symptoms_en": [
            "fever (body feeling hot)",
            "chills and shivering",
            "sweating after fever",
            "headache",
            "body and joint aches",
            "nausea or vomiting",
            "extreme tiredness"
        ],
        "red_flags_sw": [
            "kuchanganyikiwa au kupoteza fahamu",
            "macho ya njano (jaundice)",
            "degedege/mshtuko",
            "kupumua kwa shida",
            "mkojo mweusi"
        ],
        "red_flags_en": [
            "confusion or unconsciousness",
            "yellow eyes (jaundice)",
            "seizures/convulsions",
            "difficulty breathing",
            "dark/blackish urine"
        ],
        "first_aid_sw": "Kunywa maji mengi, pumzika. Fika kupima damu - USITUMIE dawa bila kupimwa.",
        "first_aid_en": "Drink lots of water, rest. Get blood test - DON'T take medicine without testing.",
        "severity_keywords": ["degedege", "fahamu", "njano", "seizure", "unconscious", "yellow"],
    },

    # =========================================================================
    # TYPHOID - Stomach infection
    # =========================================================================
    "typhoid": {
        "name_sw": "Typhoid (Homa ya Matumbo)",
        "name_en": "Typhoid Fever",
        "symptoms_sw": [
            "homa inayoongezeka polepole",
            "maumivu ya kichwa makali",
            "maumivu ya tumbo",
            "kuvimbiwa au kuhara",
            "uchovu na udhaifu",
            "upele mwekundu kifuani"
        ],
        "symptoms_en": [
            "fever that gradually increases",
            "severe headache",
            "stomach pain",
            "constipation or diarrhea",
            "fatigue and weakness",
            "rose-colored spots on chest"
        ],
        "red_flags_sw": [
            "damu kwenye choo",
            "tumbo kuvimba na kuuma sana",
            "kuchanganyikiwa"
        ],
        "red_flags_en": [
            "blood in stool",
            "severe abdominal swelling",
            "confusion"
        ],
        "first_aid_sw": "Kunywa maji safi yaliyochemshwa, kula chakula chepesi, pumzika. Fika hospitali kwa vipimo.",
        "first_aid_en": "Drink boiled clean water, eat light food, rest. Visit hospital for tests.",
        "severity_keywords": ["damu", "tumbo kuvimba", "blood", "swelling"],
    },

    # =========================================================================
    # PNEUMONIA - Lung infection
    # =========================================================================
    "pneumonia": {
        "name_sw": "Nimonia (Homa ya Mapafu)",
        "name_en": "Pneumonia",
        "symptoms_sw": [
            "kikohozi kikali na makohozi",
            "homa na kutetemeka",
            "kupumua haraka au kwa shida",
            "maumivu ya kifua unapopumua",
            "uchovu mkubwa",
            "makohozi ya njano/kijani"
        ],
        "symptoms_en": [
            "severe cough with phlegm",
            "fever and chills",
            "fast or difficult breathing",
            "chest pain when breathing",
            "extreme fatigue",
            "yellow/green mucus"
        ],
        "red_flags_sw": [
            "mbavu zinaingia ndani wakati wa kupumua",
            "midomo au kucha za bluu",
            "kushindwa kulala kwa shida ya kupumua",
            "mtoto kukataa kunyonya"
        ],
        "red_flags_en": [
            "ribs pulling in when breathing",
            "blue lips or nails",
            "can't sleep due to breathing difficulty",
            "child refusing to feed"
        ],
        "first_aid_sw": "Msaidie kukaa wima, hakikisha hewa safi, mpe maji ya uvuguvugu. Fika kituo cha afya haraka.",
        "first_aid_en": "Help sit upright, ensure fresh air, give warm fluids. Get to health center quickly.",
        "severity_keywords": ["mbavu", "bluu", "ribs", "blue", "kunyonya", "feed"],
    },

    # =========================================================================
    # TB - Tuberculosis
    # =========================================================================
    "tuberculosis": {
        "name_sw": "Kifua Kikuu (TB)",
        "name_en": "Tuberculosis (TB)",
        "symptoms_sw": [
            "kikohozi wiki 2+ kisichopona",
            "kukohoa damu au makohozi",
            "kupoteza uzito bila sababu",
            "jasho la usiku",
            "homa ya jioni",
            "uchovu wa kudumu"
        ],
        "symptoms_en": [
            "cough 2+ weeks that won't heal",
            "coughing blood or phlegm",
            "unexplained weight loss",
            "night sweats",
            "evening fever",
            "persistent fatigue"
        ],
        "red_flags_sw": [
            "kukohoa damu nyingi",
            "kupumua kwa shida kubwa",
            "kupoteza uzito haraka"
        ],
        "red_flags_en": [
            "coughing lots of blood",
            "severe breathing difficulty",
            "rapid weight loss"
        ],
        "first_aid_sw": "Afunike mdomo anapokohoa, hewa safi ndani. TB INATIBIKA - dawa ni bure serikalini!",
        "first_aid_en": "Cover mouth when coughing, good ventilation. TB IS CURABLE - medicine is free!",
        "severity_keywords": ["damu", "blood", "weight loss", "uzito"],
    },

    # =========================================================================
    # DIARRHEA - Dehydration risk
    # =========================================================================
    "diarrhea": {
        "name_sw": "Kuhara na Upungufu wa Maji",
        "name_en": "Diarrhea and Dehydration",
        "symptoms_sw": [
            "choo cha maji mara 3+ kwa siku",
            "maumivu ya tumbo",
            "kichefuchefu au kutapika",
            "kiu kali",
            "uchovu na udhaifu",
            "mkojo mchache wa njano"
        ],
        "symptoms_en": [
            "watery stool 3+ times per day",
            "stomach pain",
            "nausea or vomiting",
            "extreme thirst",
            "fatigue and weakness",
            "dark yellow urine"
        ],
        "red_flags_sw": [
            "macho kuingia ndani (yamezama)",
            "ngozi ikivutwa hairudi haraka",
            "choo chenye damu",
            "kutapika kila kitu",
            "hakuna mkojo saa 6+"
        ],
        "red_flags_en": [
            "sunken eyes",
            "skin pinch returns slowly",
            "bloody stool",
            "can't keep fluids down",
            "no urine for 6+ hours"
        ],
        "first_aid_sw": "MUHIMU: ORS (Maji 1L + sukari vijiko 6 + chumvi 1/2) kila baada ya choo. Fika leo ukiendelea.",
        "first_aid_en": "IMPORTANT: ORS (1L water + 6 tsp sugar + 1/2 tsp salt) after every stool. Go today if continues.",
        "severity_keywords": ["yamezama", "sunken", "damu", "blood", "mkojo", "urine"],
    },

    # =========================================================================
    # CHOLERA - Emergency diarrhea
    # =========================================================================
    "cholera": {
        "name_sw": "Kipindupindu (Cholera)",
        "name_en": "Cholera",
        "symptoms_sw": [
            "kuhara maji mengi kama mchele",
            "kutapika sana",
            "kiu kali sana",
            "miguu kuuma (cramps)",
            "kupoteza nguvu haraka"
        ],
        "symptoms_en": [
            "severe watery diarrhea (rice-water)",
            "severe vomiting",
            "intense thirst",
            "leg cramps",
            "rapid weakness"
        ],
        "red_flags_sw": [
            "macho yamezama",
            "ngozi hairudi",
            "hakuna mkojo",
            "mapigo dhaifu"
        ],
        "red_flags_en": [
            "sunken eyes",
            "skin stays pinched",
            "no urination",
            "weak pulse"
        ],
        "first_aid_sw": "DHARURA: Mpe ORS SASA! Hospitali HARAKA - hali inaweza kuwa mbaya ndani ya masaa.",
        "first_aid_en": "EMERGENCY: Give ORS NOW! Hospital FAST - condition can worsen in hours.",
        "severity_keywords": ["yamezama", "sunken", "hairudi", "pinched"],
    },

    # =========================================================================
    # HIGH BLOOD PRESSURE
    # =========================================================================
    "bp": {
        "name_sw": "Presha (Shinikizo la Damu)",
        "name_en": "High Blood Pressure",
        "symptoms_sw": [
            "maumivu ya kichwa (kisogoni)",
            "kizunguzungu",
            "maono kufifia",
            "moyo kwenda kasi",
            "damu kutoka puani",
            "uchovu wa ghafla"
        ],
        "symptoms_en": [
            "headache (back of head)",
            "dizziness",
            "blurred vision",
            "fast heartbeat",
            "nosebleed",
            "sudden fatigue"
        ],
        "red_flags_sw": [
            "ganzi upande mmoja wa mwili",
            "uso kulegea upande mmoja",
            "kushindwa kuongea ghafla",
            "maumivu makali ya kifua",
            "kupoteza fahamu"
        ],
        "red_flags_en": [
            "numbness on one side",
            "face drooping on one side",
            "sudden speech difficulty",
            "severe chest pain",
            "loss of consciousness"
        ],
        "first_aid_sw": "Pumzika, fungua nguo zinazobana, epuka chumvi. Ganzi/uso kulegea = KIHARUSI - hospitali SASA!",
        "first_aid_en": "Rest, loosen tight clothes, avoid salt. Numbness/face drooping = STROKE - hospital NOW!",
        "severity_keywords": ["ganzi", "numbness", "uso kulegea", "face drooping", "chest pain", "kifua"],
    },

    # =========================================================================
    # DIABETES
    # =========================================================================
    "diabetes": {
        "name_sw": "Kisukari",
        "name_en": "Diabetes",
        "symptoms_sw": [
            "kukojoa mara kwa mara",
            "kiu sana",
            "njaa sana",
            "kupoteza uzito bila sababu",
            "uchovu",
            "vidonda visivyopona",
            "kuona vibaya"
        ],
        "symptoms_en": [
            "frequent urination",
            "excessive thirst",
            "excessive hunger",
            "unexplained weight loss",
            "fatigue",
            "slow healing wounds",
            "blurry vision"
        ],
        "red_flags_sw": [
            "kupoteza fahamu",
            "kupumua haraka na kwa kina",
            "harufu ya matunda mdomoni",
            "kutetemeka na jasho sana"
        ],
        "red_flags_en": [
            "loss of consciousness",
            "fast deep breathing",
            "fruity breath smell",
            "severe shaking and sweating"
        ],
        "first_aid_sw": "Sukari CHINI (kutetemeka/jasho): Mpe juice/sukari HARAKA. Hospitali kama hana fahamu.",
        "first_aid_en": "LOW sugar (shaking/sweating): Give juice/sugar FAST. Hospital if unconscious.",
        "severity_keywords": ["fahamu", "unconscious", "kutetemeka", "shaking"],
    },

    # =========================================================================
    # PREGNANCY COMPLICATIONS
    # =========================================================================
    "pregnancy": {
        "name_sw": "Matatizo ya Ujauzito",
        "name_en": "Pregnancy Complications",
        "symptoms_sw": [
            "damu kutoka ukeni",
            "maumivu makali ya tumbo",
            "homa",
            "kuvimba miguu na uso sana",
            "kichwa kuuma sana",
            "kuona vibaya"
        ],
        "symptoms_en": [
            "vaginal bleeding",
            "severe stomach pain",
            "fever",
            "severe swelling of feet and face",
            "severe headache",
            "vision problems"
        ],
        "red_flags_sw": [
            "damu nyingi ukeni",
            "maumivu makali ya tumbo",
            "mtoto hasogei siku nzima",
            "degedege",
            "kupumua kwa shida"
        ],
        "red_flags_en": [
            "heavy vaginal bleeding",
            "severe abdominal pain",
            "baby not moving all day",
            "seizures",
            "breathing difficulty"
        ],
        "first_aid_sw": "Dalili hizi ni HATARI kwa mama na mtoto. Fika HOSPITALI SASA - usisubiri!",
        "first_aid_en": "These signs are DANGEROUS for mother and baby. Go to HOSPITAL NOW - don't wait!",
        "severity_keywords": ["damu", "blood", "hasogei", "not moving", "degedege", "seizure"],
    },

    # =========================================================================
    # CHILD ILLNESS
    # =========================================================================
    "child": {
        "name_sw": "Mtoto Mgonjwa",
        "name_en": "Sick Child",
        "symptoms_sw": [
            "homa",
            "kikohozi",
            "kuhara",
            "kutapika",
            "kulia sana",
            "kukataa kula"
        ],
        "symptoms_en": [
            "fever",
            "cough",
            "diarrhea",
            "vomiting",
            "excessive crying",
            "refusing to eat"
        ],
        "red_flags_sw": [
            "homa kali + degedege",
            "kukataa kunyonya kabisa",
            "kulala sana/kutoamka",
            "kupumua kwa shida",
            "fontanel (utosi) kuzama"
        ],
        "red_flags_en": [
            "high fever + seizures",
            "completely refusing to breastfeed",
            "very sleepy/can't wake",
            "breathing difficulty",
            "sunken fontanel"
        ],
        "first_aid_sw": "Dalili hizi ni HATARI kwa mtoto. Mpeleke HOSPITALI HARAKA - watoto hawasubiri!",
        "first_aid_en": "These signs are DANGEROUS for child. Take to HOSPITAL FAST - children can't wait!",
        "severity_keywords": ["degedege", "seizure", "kunyonya", "feed", "kupumua", "breath"],
    },

    # =========================================================================
    # DIZZINESS/FAINTING
    # =========================================================================
    "dizziness": {
        "name_sw": "Kizunguzungu/Kuishiwa Nguvu",
        "name_en": "Dizziness/Fainting",
        "symptoms_sw": [
            "kizunguzungu",
            "kuona kiza",
            "kuishiwa nguvu",
            "kuhisi kuanguka",
            "moyo kwenda haraka",
            "jasho baridi"
        ],
        "symptoms_en": [
            "dizziness",
            "seeing darkness",
            "feeling weak",
            "feeling like falling",
            "fast heartbeat",
            "cold sweats"
        ],
        "red_flags_sw": [
            "kupoteza fahamu",
            "ganzi upande mmoja",
            "kifua kuuma",
            "kupumua kwa shida"
        ],
        "red_flags_en": [
            "loss of consciousness",
            "numbness on one side",
            "chest pain",
            "breathing difficulty"
        ],
        "first_aid_sw": "Inaweza kuwa presha chini au sukari chini. Lala chini SASA, kunywa maji+sukari. Pima presha na damu.",
        "first_aid_en": "Could be low BP or low sugar. Lie down NOW, drink water+sugar. Check BP and blood.",
        "severity_keywords": ["fahamu", "unconscious", "ganzi", "numbness", "kifua", "chest"],
    },
}

# =============================================================================
# SMS KEYWORD MATCHING - For disease classification
# =============================================================================

SMS_KEYWORDS = {
    "malaria": [
        "homa", "fever", "tetemeka", "shake", "baridi", "chills", "malaria",
        "mbu", "mosquito", "jasho", "sweat", "njano", "yellow", "degedege",
        "seizure", "kichwa", "headache", "mwili kuuma"
    ],
    "pneumonia": [
        "kikohozi", "cough", "pumzi", "breath", "nimonia", "pneumonia",
        "kifua", "chest", "koroma", "wheeze", "mapafu", "lung", "kohozi",
        "mucus", "mbavu", "ribs", "hema", "breathing"
    ],
    "diarrhea": [
        "kuhara", "diarrhea", "diarrhoea", "harisha", "kutapika", "vomit",
        "tumbo", "stomach", "kipindupindu", "cholera", "ors", "maji",
        "choo", "damu", "majimaji", "watery"
    ],
    "bp": [
        "shinikizo", "pressure", "bp", "kizunguzungu", "dizzy", "kichwa",
        "headache", "kiharusi", "stroke", "ganzi", "numb", "moyo", "heart",
        "damu", "blood", "presha", "kisogo"
    ],
    "diabetes": [
        "sukari", "sugar", "kisukari", "diabetes", "kiu", "thirsty",
        "kukojoa", "urinate", "vidonda", "wounds", "kutetemeka", "shaking"
    ],
    "dizziness": [
        "kizunguzungu", "dizzy", "kuona kiza", "naona kiza", "kiza", "darkness", 
        "kuishiwa nguvu", "kuishiwa", "nguvu", "weak", "kuanguka", "falling", 
        "kuzimia", "faint", "jasho baridi", "nahisi dhaifu", "dhaifu", "kusinzia"
    ],
    "pregnancy": [
        "mjamzito", "pregnant", "mimba", "ujauzito", "pregnancy", "uzazi",
        "damu ukeni", "bleeding", "mtoto", "baby", "kichwa kuuma"
    ],
    "child": [
        "mtoto", "child", "watoto", "children", "mwanangu", "baby",
        "kunyonya", "breastfeed", "degedege", "seizure"
    ],
    "tuberculosis": [
        "kifua kikuu", "tb", "tuberculosis", "kikohozi wiki", "cough weeks",
        "damu", "blood", "jasho usiku", "night sweat", "uzito", "weight"
    ],
}


def get_disease(code: str) -> dict:
    """Get disease info by code."""
    return DISEASES.get(code, {})


def classify_sms_keywords(text: str) -> str | None:
    """Classify SMS text to disease category based on keywords."""
    text_lower = text.lower()
    scores = {d: 0 for d in SMS_KEYWORDS}
    
    for disease, keywords in SMS_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[disease] += 1
    
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None


def get_severity(disease: str, text: str) -> str:
    """Determine severity based on red flag keywords in text."""
    if disease not in DISEASES:
        return "yellow"
    
    text_lower = text.lower()
    severity_keywords = DISEASES[disease].get("severity_keywords", [])
    
    for keyword in severity_keywords:
        if keyword in text_lower:
            return "red"
    
    return "yellow"
