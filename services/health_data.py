DISEASES = {
    "malaria": {
        "name_sw": "Malaria",
        "name_en": "Malaria",
        "symptoms_sw": ["homa kali", "kutetemeka", "baridi", "maumivu ya kichwa", "uchovu"],
        "symptoms_en": ["high fever", "shaking", "chills", "headache", "fatigue"],
        "red_flags_sw": [
            "kuchanganyikiwa",
            "kushindwa kuamka",
            "macho ya njano",
            "kutapika kila kitu",
            "degedege",
        ],
        "red_flags_en": [
            "confusion",
            "cannot wake up",
            "yellow eyes",
            "vomiting everything",
            "seizures",
        ],
        "first_aid_sw": (
            "Malaria inaweza kutibiwa ukifika kituoni leo. "
            "Pata kipimo cha damu (MRDT). Kunywa maji mengi. "
            "Usitumie dawa bila kipimo cha daktari."
        ),
        "first_aid_en": (
            "Malaria can be treated if you go to a clinic today. "
            "Get a blood test (MRDT). Drink plenty of water. "
            "Do not take medicine without a proper test."
        ),
    },
    "pneumonia": {
        "name_sw": "Nimonia",
        "name_en": "Pneumonia",
        "symptoms_sw": ["kikohozi", "homa", "kupumua kwa haraka", "maumivu ya kifua"],
        "symptoms_en": ["cough", "fever", "fast breathing", "chest pain"],
        "red_flags_sw": [
            "mbavu zinaingia ndani anapopumua",
            "midomo au kucha kuwa buluu",
            "mtoto kushindwa kunyonya",
            "sauti ya kukoroma",
            "kupoteza fahamu",
        ],
        "red_flags_en": [
            "ribs visible when breathing",
            "blue lips or fingernails",
            "child cannot breastfeed",
            "grunting sound",
            "loss of consciousness",
        ],
        "first_aid_sw": (
            "Mweke mgonjwa katika hali ya utulivu na joto. "
            "Mpe maji mengi. Fika kituoni haraka kwa antibiotics."
        ),
        "first_aid_en": (
            "Keep patient calm and warm. "
            "Give plenty of fluids. Go to clinic urgently for antibiotics."
        ),
    },
    "diarrhea": {
        "name_sw": "Kuhara",
        "name_en": "Diarrhea",
        "symptoms_sw": ["kuhara majimaji", "kutapika", "maumivu ya tumbo", "kiu kali"],
        "symptoms_en": ["watery diarrhea", "vomiting", "stomach cramps", "extreme thirst"],
        "red_flags_sw": [
            "macho yamezama",
            "ngozi kutovuta",
            "kushindwa kukojoa kwa muda mrefu",
            "mdomo mkavu sana",
            "udhaifu mkubwa",
        ],
        "red_flags_en": [
            "sunken eyes",
            "skin does not bounce back",
            "not urinating for a long time",
            "very dry mouth",
            "extreme weakness",
        ],
        "first_aid_sw": (
            "Tengeneza ORS nyumbani sasa: "
            "Maji safi lita 1 + vijiko 6 sukari + nusu kijiko chumvi. "
            "Mpe kidogo kidogo mara kwa mara. Fika zahanati leo."
        ),
        "first_aid_en": (
            "Make ORS at home right now: "
            "1 litre clean water + 6 teaspoons sugar + half teaspoon salt. "
            "Give small sips often. Go to clinic today."
        ),
    },
    "bp": {
        "name_sw": "Shinikizo la Damu",
        "name_en": "High Blood Pressure",
        "symptoms_sw": [
            "kuumwa kichwa nyuma",
            "kizunguzungu",
            "kutona vizuri",
            "moyo kupiga haraka",
        ],
        "symptoms_en": [
            "pain at back of head",
            "dizziness",
            "blurry vision",
            "fast heartbeat",
        ],
        "red_flags_sw": [
            "ganzi upande mmoja wa mwili",
            "uso kulegea upande mmoja",
            "kushindwa kuongea vizuri",
            "kupoteza fahamu",
        ],
        "red_flags_en": [
            "numbness on one side of body",
            "face drooping on one side",
            "cannot speak properly",
            "loss of consciousness",
        ],
        "first_aid_sw": (
            "Pumzika sasa hivi, usiinuke haraka. "
            "Pima shinikizo la damu kituoni mapema. "
            "Punguza chumvi na msongo wa mawazo."
        ),
        "first_aid_en": (
            "Rest now, do not stand up suddenly. "
            "Check your blood pressure at a clinic soon. "
            "Reduce salt intake and avoid stress."
        ),
    },
}

# Keywords for SMS free-text classification
SMS_KEYWORDS = {
    "malaria":   ["homa", "fever", "tetemeka", "shake", "baridi", "chills", "malaria", "mbu", "mosquito"],
    "pneumonia": ["kikohozi", "cough", "pumzi", "breath", "nimonia", "pneumonia", "kifua", "chest"],
    "diarrhea":  ["kuhara", "diarrhea", "diarrhoea", "harisha", "kutapika", "vomit", "tumbo", "stomach", "kipindupindu"],
    "bp":        ["shinikizo", "pressure", "bp", "kizunguzungu", "dizzy", "kichwa", "headache", "kiharusi", "stroke"],
}


def get_disease(code: str) -> dict:
    return DISEASES.get(code, {})


def classify_sms_keywords(text: str) -> str | None:
    text_lower = text.lower()
    scores = {d: 0 for d in SMS_KEYWORDS}
    for disease, keywords in SMS_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[disease] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None
