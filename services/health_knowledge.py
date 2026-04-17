"""
AfyaMkononi Health Knowledge Base
Comprehensive medical information for AI-powered health guidance.

Sources:
- WHO Guidelines for Malaria, IMCI, Maternal Health
- CDC Clinical Guidelines
- Mayo Clinic Medical References
- MSF Clinical Guidelines

NOTE: This is for first-aid guidance only. Always recommend professional care.
"""

# =============================================================================
# DISEASE KNOWLEDGE BASE - Accurate, research-based information
# =============================================================================

HEALTH_KNOWLEDGE = {
    # -------------------------------------------------------------------------
    # MALARIA / HOMA
    # -------------------------------------------------------------------------
    "malaria": {
        "names": {
            "sw": "Malaria (Homa ya Malaria)",
            "en": "Malaria"
        },
        "description": {
            "sw": "Ugonjwa unaosababishwa na vimelea vinavyoenezwa na mbu. Ni ugonjwa wa kawaida Afrika Mashariki.",
            "en": "Disease caused by parasites spread through mosquito bites. Common in East Africa."
        },
        "symptoms": {
            "sw": [
                "Homa inayokuja na kuondoka",
                "Baridi na kutetemeka mwili",
                "Jasho jingi",
                "Maumivu ya kichwa",
                "Maumivu ya mwili na viungo",
                "Kichefuchefu au kutapika",
                "Uchovu mkubwa"
            ],
            "en": [
                "Fever that comes and goes",
                "Chills and shivering",
                "Heavy sweating",
                "Headache",
                "Body and joint pain",
                "Nausea or vomiting",
                "Severe fatigue"
            ]
        },
        "danger_signs": {
            "sw": [
                "Kuchanganyikiwa au kupoteza fahamu",
                "Macho ya njano (jaundice)",
                "Degedege/mshtuko",
                "Kupumua kwa shida",
                "Kutapika damu"
            ],
            "en": [
                "Confusion or unconsciousness",
                "Yellow eyes (jaundice)",
                "Seizures/convulsions",
                "Difficulty breathing",
                "Vomiting blood"
            ]
        },
        "first_aid": {
            "sw": [
                "Mpumzishe mgonjwa mahali penye hewa",
                "Mpe maji mengi ya kunywa",
                "Punguza joto kwa kitambaa cha maji baridi",
                "Usimpe aspirin - inaweza kudhuru",
                "Fika kituo cha afya kwa kipimo cha malaria"
            ],
            "en": [
                "Rest the patient in a well-ventilated area",
                "Give plenty of fluids to drink",
                "Reduce fever with cool wet cloth",
                "Do not give aspirin - can be harmful",
                "Visit health center for malaria test"
            ]
        },
        "prevention": {
            "sw": "Tumia chandarua, dawa ya kufukuza mbu, na ondoa maji yaliyotuama.",
            "en": "Use bed nets, mosquito repellent, and remove stagnant water."
        }
    },

    # -------------------------------------------------------------------------
    # TYPHOID / HOMA YA MATUMBO
    # -------------------------------------------------------------------------
    "typhoid": {
        "names": {
            "sw": "Typhoid (Homa ya Matumbo)",
            "en": "Typhoid Fever"
        },
        "description": {
            "sw": "Ugonjwa wa bakteria unaosababishwa na maji au chakula chafu.",
            "en": "Bacterial infection caused by contaminated food or water."
        },
        "symptoms": {
            "sw": [
                "Homa inayoongezeka polepole",
                "Maumivu ya kichwa makali",
                "Maumivu ya tumbo",
                "Kuvimbiwa au kuhara",
                "Uchovu na udhaifu",
                "Upele mwekundu kifuani"
            ],
            "en": [
                "Fever that gradually increases",
                "Severe headache",
                "Stomach pain",
                "Constipation or diarrhea",
                "Fatigue and weakness",
                "Rose-colored spots on chest"
            ]
        },
        "danger_signs": {
            "sw": [
                "Damu kwenye choo",
                "Tumbo kuvimba na kuuma sana",
                "Kuchanganyikiwa"
            ],
            "en": [
                "Blood in stool",
                "Severe abdominal swelling and pain",
                "Confusion"
            ]
        },
        "first_aid": {
            "sw": [
                "Mpe maji mengi safi ya kuchemshwa",
                "Mpe chakula chepesi",
                "Mpumzishe mgonjwa",
                "Fika hospitali kwa vipimo na dawa"
            ],
            "en": [
                "Give plenty of boiled clean water",
                "Give light, easy-to-digest food",
                "Let patient rest",
                "Visit hospital for tests and treatment"
            ]
        },
        "prevention": {
            "sw": "Kunywa maji safi yaliyochemshwa, osha mikono, kula chakula kilichopikwa vizuri.",
            "en": "Drink boiled clean water, wash hands, eat well-cooked food."
        }
    },

    # -------------------------------------------------------------------------
    # CHOLERA / KIPINDUPINDU
    # -------------------------------------------------------------------------
    "cholera": {
        "names": {
            "sw": "Kipindupindu (Cholera)",
            "en": "Cholera"
        },
        "description": {
            "sw": "Ugonjwa hatari wa kuhara maji mengi unaosababishwa na bakteria kwenye maji machafu.",
            "en": "Dangerous diarrheal disease caused by bacteria in contaminated water."
        },
        "symptoms": {
            "sw": [
                "Kuhara maji mengi kama mchele",
                "Kutapika sana",
                "Kiu kali",
                "Mguu kuuma (cramps)",
                "Kupoteza nguvu haraka"
            ],
            "en": [
                "Severe watery diarrhea (rice-water stool)",
                "Severe vomiting",
                "Intense thirst",
                "Leg cramps",
                "Rapid loss of strength"
            ]
        },
        "danger_signs": {
            "sw": [
                "Macho yamezama ndani",
                "Ngozi inapokunjwa hairudi",
                "Hakuna mkojo",
                "Mapigo ya moyo dhaifu"
            ],
            "en": [
                "Sunken eyes",
                "Skin pinch goes back slowly",
                "No urination",
                "Weak pulse"
            ]
        },
        "first_aid": {
            "sw": [
                "MUHIMU: Mpe ORS mara moja!",
                "Kama hakuna ORS: Maji 1L + sukari vijiko 6 + chumvi kijiko 1/2",
                "Mpe kidogo kidogo mara kwa mara",
                "Fika hospitali HARAKA - hali inaweza kuwa mbaya ndani ya masaa"
            ],
            "en": [
                "IMPORTANT: Give ORS immediately!",
                "If no ORS: 1L water + 6 tsp sugar + 1/2 tsp salt",
                "Give small amounts frequently",
                "Get to hospital FAST - condition can worsen in hours"
            ]
        },
        "prevention": {
            "sw": "Kunywa maji safi, osha mikono na sabuni, kula chakula kilichopikwa.",
            "en": "Drink clean water, wash hands with soap, eat cooked food."
        }
    },

    # -------------------------------------------------------------------------
    # PNEUMONIA / NIMONIA
    # -------------------------------------------------------------------------
    "pneumonia": {
        "names": {
            "sw": "Nimonia (Maambukizi ya Mapafu)",
            "en": "Pneumonia (Lung Infection)"
        },
        "description": {
            "sw": "Maambukizi ya mapafu yanayosababisha shida ya kupumua.",
            "en": "Lung infection that causes breathing difficulties."
        },
        "symptoms": {
            "sw": [
                "Kikohozi kikali (kinaweza kuwa na makohozi)",
                "Homa",
                "Kupumua haraka",
                "Maumivu kifuani unapopumua",
                "Uchovu na udhaifu"
            ],
            "en": [
                "Severe cough (may have phlegm)",
                "Fever",
                "Fast breathing",
                "Chest pain when breathing",
                "Fatigue and weakness"
            ]
        },
        "danger_signs": {
            "sw": [
                "Mbavu zinaingia ndani wakati wa kupumua",
                "Midomo au kucha za bluu",
                "Kushindwa kulala kwa shida ya kupumua",
                "Kushindwa kunywa au kula"
            ],
            "en": [
                "Ribs pulling in when breathing",
                "Blue lips or fingernails",
                "Unable to sleep due to breathing difficulty",
                "Unable to drink or eat"
            ]
        },
        "first_aid": {
            "sw": [
                "Msaidie kukaa wima au nusu-wima",
                "Hakikisha ana hewa safi",
                "Mpe maji ya uvuguvugu (sio baridi)",
                "Mfunike ili awe na joto",
                "Fika kituo cha afya haraka"
            ],
            "en": [
                "Help them sit upright or semi-upright",
                "Ensure fresh air circulation",
                "Give warm fluids (not cold)",
                "Keep them warm with blankets",
                "Get to health center quickly"
            ]
        },
        "prevention": {
            "sw": "Chanjo, hewa safi ndani ya nyumba, epuka msongamano.",
            "en": "Vaccination, good indoor ventilation, avoid crowded places."
        }
    },

    # -------------------------------------------------------------------------
    # TUBERCULOSIS / KIFUA KIKUU
    # -------------------------------------------------------------------------
    "tuberculosis": {
        "names": {
            "sw": "Kifua Kikuu (TB)",
            "en": "Tuberculosis (TB)"
        },
        "description": {
            "sw": "Ugonjwa wa bakteria unaoshambulia mapafu, unaenezwa kwa hewa.",
            "en": "Bacterial disease affecting lungs, spread through air."
        },
        "symptoms": {
            "sw": [
                "Kikohozi cha wiki 2+ kisichopona",
                "Kukohoa damu au makohozi",
                "Kupoteza uzito bila sababu",
                "Jasho la usiku",
                "Homa ya jioni",
                "Uchovu wa kudumu"
            ],
            "en": [
                "Cough lasting 2+ weeks that won't heal",
                "Coughing blood or phlegm",
                "Unexplained weight loss",
                "Night sweats",
                "Evening fever",
                "Persistent fatigue"
            ]
        },
        "danger_signs": {
            "sw": [
                "Kukohoa damu nyingi",
                "Kupumua kwa shida kubwa",
                "Kupoteza uzito haraka"
            ],
            "en": [
                "Coughing up lots of blood",
                "Severe breathing difficulty",
                "Rapid weight loss"
            ]
        },
        "first_aid": {
            "sw": [
                "Mgonjwa afunike mdomo anapokohoa",
                "Hakikisha hewa safi ndani",
                "Fika kituo cha afya kwa kipimo cha TB",
                "TB INATIBIKA! Dawa ni bure serikalini"
            ],
            "en": [
                "Patient should cover mouth when coughing",
                "Ensure good ventilation indoors",
                "Visit health center for TB test",
                "TB IS CURABLE! Medicine is free from government"
            ]
        },
        "prevention": {
            "sw": "Chanjo ya BCG kwa watoto, hewa safi, epuka msongamano.",
            "en": "BCG vaccination for children, good ventilation, avoid crowded places."
        }
    },

    # -------------------------------------------------------------------------
    # DIARRHEA / KUHARA
    # -------------------------------------------------------------------------
    "diarrhea": {
        "names": {
            "sw": "Kuhara",
            "en": "Diarrhea"
        },
        "description": {
            "sw": "Hali ya kwenda haja kubwa maji mara nyingi kwa siku.",
            "en": "Condition of passing watery stool multiple times a day."
        },
        "symptoms": {
            "sw": [
                "Choo cha maji mara 3+ kwa siku",
                "Maumivu ya tumbo",
                "Kiu",
                "Udhaifu"
            ],
            "en": [
                "Watery stool 3+ times per day",
                "Stomach pain",
                "Thirst",
                "Weakness"
            ]
        },
        "danger_signs": {
            "sw": [
                "Macho yamezama",
                "Ngozi hairudi inapovutwa",
                "Hakuna machozi wala mkojo",
                "Damu kwenye choo",
                "Homa kali"
            ],
            "en": [
                "Sunken eyes",
                "Skin stays pinched when pulled",
                "No tears or urination",
                "Blood in stool",
                "High fever"
            ]
        },
        "first_aid": {
            "sw": [
                "Mpe ORS au maji+sukari+chumvi MARA MOJA",
                "Endelea kunyonyesha mtoto",
                "Mpe chakula chepesi anapoweza",
                "Usipe dawa za kusimamisha kuhara",
                "Fika kituo cha afya kama hali haibadiliki"
            ],
            "en": [
                "Give ORS or water+sugar+salt IMMEDIATELY",
                "Continue breastfeeding if child",
                "Give light food when able to eat",
                "Do not give anti-diarrhea medicine",
                "Visit clinic if condition doesn't improve"
            ]
        },
        "prevention": {
            "sw": "Kunywa maji safi, osha mikono, kula chakula kilichopikwa.",
            "en": "Drink clean water, wash hands, eat cooked food."
        }
    },

    # -------------------------------------------------------------------------
    # HIGH BLOOD PRESSURE / PRESHA
    # -------------------------------------------------------------------------
    "hypertension": {
        "names": {
            "sw": "Presha (Shinikizo la Damu)",
            "en": "High Blood Pressure (Hypertension)"
        },
        "description": {
            "sw": "Hali ambapo damu inasukuma kwa nguvu kupita kawaida kwenye mishipa.",
            "en": "Condition where blood pushes too hard against blood vessel walls."
        },
        "symptoms": {
            "sw": [
                "Mara nyingi hakuna dalili (silent killer)",
                "Maumivu ya kichwa (hasa kisogoni)",
                "Kizunguzungu",
                "Kupumua kwa shida",
                "Damu kutoka puani"
            ],
            "en": [
                "Often no symptoms (silent killer)",
                "Headache (especially back of head)",
                "Dizziness",
                "Shortness of breath",
                "Nosebleeds"
            ]
        },
        "danger_signs": {
            "sw": [
                "Ganzi au kufa ganzi upande mmoja",
                "Uso kulegea upande mmoja",
                "Kushindwa kuongea vizuri ghafla",
                "Maumivu makali ya kifua",
                "Kuona kiza au macho kuona vibaya ghafla"
            ],
            "en": [
                "Numbness or weakness on one side",
                "Face drooping on one side",
                "Sudden difficulty speaking",
                "Severe chest pain",
                "Sudden vision problems"
            ]
        },
        "first_aid": {
            "sw": [
                "Mkalie chini mahali pa utulivu",
                "Fungua nguo zinazobana",
                "Pumzika - usifanye kazi nzito",
                "Epuka chumvi na mafuta",
                "Fika kituo cha afya kupima BP"
            ],
            "en": [
                "Sit them down in a quiet place",
                "Loosen tight clothing",
                "Rest - avoid physical exertion",
                "Avoid salt and fatty foods",
                "Visit clinic to check BP"
            ]
        },
        "prevention": {
            "sw": "Punguza chumvi, fanya mazoezi, epuka pombe na sigara, pima BP mara kwa mara.",
            "en": "Reduce salt, exercise regularly, avoid alcohol and smoking, check BP regularly."
        }
    },

    # -------------------------------------------------------------------------
    # DIABETES / KISUKARI
    # -------------------------------------------------------------------------
    "diabetes": {
        "names": {
            "sw": "Kisukari (Ugonjwa wa Sukari)",
            "en": "Diabetes"
        },
        "description": {
            "sw": "Hali ambapo mwili hauwezi kudhibiti sukari kwenye damu vizuri.",
            "en": "Condition where body cannot properly control blood sugar levels."
        },
        "symptoms": {
            "sw": [
                "Kukojoa mara kwa mara",
                "Kiu sana",
                "Njaa sana",
                "Kupoteza uzito bila sababu",
                "Uchovu",
                "Vidonda visivyopona",
                "Kuona vibaya"
            ],
            "en": [
                "Frequent urination",
                "Excessive thirst",
                "Excessive hunger",
                "Unexplained weight loss",
                "Fatigue",
                "Wounds that don't heal",
                "Blurry vision"
            ]
        },
        "danger_signs": {
            "sw": [
                "Kupoteza fahamu",
                "Kupumua haraka na kwa kina",
                "Harufu ya matunda mdomoni",
                "Kutetemeka na jasho (sukari chini)",
                "Kuchanganyikiwa"
            ],
            "en": [
                "Loss of consciousness",
                "Fast and deep breathing",
                "Fruity smell on breath",
                "Shaking and sweating (low sugar)",
                "Confusion"
            ]
        },
        "first_aid": {
            "sw": [
                "Kama ana tetemeka/jasho (sukari chini): Mpe sukari au juice",
                "Kama hana fahamu: Usimpe chochote mdomoni",
                "Mlalize kwa ubavu",
                "Fika hospitali HARAKA"
            ],
            "en": [
                "If shaking/sweating (low sugar): Give sugar or juice",
                "If unconscious: Do not give anything by mouth",
                "Lay them on their side",
                "Get to hospital FAST"
            ]
        },
        "prevention": {
            "sw": "Kula vizuri, fanya mazoezi, punguza sukari na wanga, pima sukari mara kwa mara.",
            "en": "Eat well, exercise, reduce sugar and carbs, check blood sugar regularly."
        }
    },

    # -------------------------------------------------------------------------
    # PREGNANCY COMPLICATIONS / MATATIZO YA UJAUZITO
    # -------------------------------------------------------------------------
    "pregnancy": {
        "names": {
            "sw": "Matatizo ya Ujauzito",
            "en": "Pregnancy Complications"
        },
        "description": {
            "sw": "Dalili za hatari wakati wa ujauzito ambazo zinahitaji msaada wa haraka.",
            "en": "Danger signs during pregnancy that need immediate attention."
        },
        "symptoms": {
            "sw": [
                "Kutoka damu ukeni",
                "Maumivu makali ya tumbo",
                "Homa",
                "Kuvimba miguu na uso sana",
                "Maumivu ya kichwa makali",
                "Kuona vibaya au kiza"
            ],
            "en": [
                "Vaginal bleeding",
                "Severe abdominal pain",
                "Fever",
                "Severe swelling of feet and face",
                "Severe headache",
                "Vision problems or seeing darkness"
            ]
        },
        "danger_signs": {
            "sw": [
                "Kutoka damu nyingi",
                "Mtoto hasogei tena",
                "Degedege/mshtuko",
                "Kupoteza fahamu",
                "Maji kuvunjika mapema"
            ],
            "en": [
                "Heavy bleeding",
                "Baby not moving anymore",
                "Seizures/convulsions",
                "Loss of consciousness",
                "Water breaking early"
            ]
        },
        "first_aid": {
            "sw": [
                "Mlaze upande wa kushoto",
                "Usimpe chakula wala kinywaji kama anaweza kwenda theatre",
                "Fika hospitali SASA - hii ni dharura",
                "Kama damu nyingi: Beba pedi za ziada"
            ],
            "en": [
                "Lay her on left side",
                "No food or drink if she may need surgery",
                "Get to hospital NOW - this is emergency",
                "If heavy bleeding: Bring extra pads"
            ]
        },
        "prevention": {
            "sw": "Hudhuria kliniki ya wajawazito, kula vizuri, pumzika, pima BP.",
            "en": "Attend antenatal clinic, eat well, rest, check BP."
        }
    },

    # -------------------------------------------------------------------------
    # CHILD ILLNESS / MAGONJWA YA WATOTO
    # -------------------------------------------------------------------------
    "child_illness": {
        "names": {
            "sw": "Magonjwa ya Watoto",
            "en": "Child Illness"
        },
        "description": {
            "sw": "Dalili muhimu za kuangalia kwa watoto wagonjwa.",
            "en": "Important signs to watch in sick children."
        },
        "symptoms": {
            "sw": [
                "Homa",
                "Kikohozi",
                "Kuhara",
                "Kutapika",
                "Kukataa kula au kunyonya"
            ],
            "en": [
                "Fever",
                "Cough",
                "Diarrhea",
                "Vomiting",
                "Refusing to eat or breastfeed"
            ]
        },
        "danger_signs": {
            "sw": [
                "Hawezi kunyonya au kunywa",
                "Anatapika kila kitu",
                "Degedege/mshtuko",
                "Ana usingizi sana - hawezi kuamshwa",
                "Kupumua kwa shida - mbavu zinaingia"
            ],
            "en": [
                "Cannot breastfeed or drink",
                "Vomits everything",
                "Seizures/convulsions",
                "Very sleepy - cannot be woken",
                "Difficulty breathing - ribs pulling in"
            ]
        },
        "first_aid": {
            "sw": [
                "Endelea kumnyonyesha au kumpa maji",
                "Punguza joto kwa kitambaa cha maji baridi",
                "Kama kuhara: Mpe ORS",
                "Usimpe dawa za watu wazima",
                "Fika kituo cha afya HARAKA kama una wasiwasi"
            ],
            "en": [
                "Continue breastfeeding or giving fluids",
                "Reduce fever with cool wet cloth",
                "If diarrhea: Give ORS",
                "Do not give adult medicine",
                "Get to clinic FAST if worried"
            ]
        },
        "prevention": {
            "sw": "Chanjo kamili, usafi, lishe bora, kunyonyesha.",
            "en": "Complete vaccination, hygiene, good nutrition, breastfeeding."
        }
    },

    # -------------------------------------------------------------------------
    # GENERAL DIZZINESS / KIZUNGUZUNGU
    # -------------------------------------------------------------------------
    "dizziness": {
        "names": {
            "sw": "Kizunguzungu",
            "en": "Dizziness"
        },
        "description": {
            "sw": "Hisia ya kuzunguka au kupoteza usawa. Inaweza kusababishwa na mambo mengi.",
            "en": "Feeling of spinning or losing balance. Can be caused by many things."
        },
        "possible_causes": {
            "sw": [
                "Presha ya chini au ya juu",
                "Upungufu wa damu (anemia)",
                "Sukari ya chini",
                "Upungufu wa maji mwilini",
                "Maambukizi ya sikio",
                "Msongo wa mawazo",
                "Kutokulala vizuri"
            ],
            "en": [
                "Low or high blood pressure",
                "Low blood (anemia)",
                "Low blood sugar",
                "Dehydration",
                "Inner ear infection",
                "Stress or anxiety",
                "Lack of sleep"
            ]
        },
        "danger_signs": {
            "sw": [
                "Ganzi au kufa ganzi upande mmoja wa mwili",
                "Kushindwa kuongea vizuri",
                "Maumivu makali ya kichwa",
                "Kifua kuuma",
                "Kupoteza fahamu",
                "Kuona kiza au macho kuona vibaya ghafla"
            ],
            "en": [
                "Numbness or weakness on one side of body",
                "Difficulty speaking",
                "Severe headache",
                "Chest pain",
                "Loss of consciousness",
                "Sudden vision problems"
            ]
        },
        "first_aid": {
            "sw": [
                "Kaa chini au lala - usisimame",
                "Kunywa maji polepole",
                "Kula kitu kidogo kama hujala",
                "Pumzika mahali penye hewa",
                "Kama dalili zinaendelea au ni kali - fika hospitali"
            ],
            "en": [
                "Sit or lie down - don't stand",
                "Drink water slowly",
                "Eat something if you haven't eaten",
                "Rest in a ventilated place",
                "If symptoms persist or are severe - go to hospital"
            ]
        },
        "prevention": {
            "sw": "Kula mara kwa mara, kunywa maji, lala vizuri, simama polepole.",
            "en": "Eat regularly, stay hydrated, sleep well, stand up slowly."
        }
    }
}

# =============================================================================
# SYMPTOM TO POSSIBLE CONDITIONS MAPPING
# =============================================================================

SYMPTOM_CONDITIONS = {
    # Swahili symptoms
    "homa": ["malaria", "typhoid", "pneumonia", "tuberculosis"],
    "joto": ["malaria", "typhoid", "pneumonia"],
    "baridi": ["malaria"],
    "kutetemeka": ["malaria", "diabetes"],
    "kichwa": ["malaria", "typhoid", "hypertension", "dizziness"],
    "kizunguzungu": ["hypertension", "diabetes", "dizziness", "anemia"],
    "kikohozi": ["pneumonia", "tuberculosis"],
    "pumzi": ["pneumonia", "tuberculosis", "hypertension"],
    "kuhara": ["cholera", "diarrhea", "typhoid"],
    "kutapika": ["cholera", "malaria", "pregnancy"],
    "tumbo": ["typhoid", "diarrhea", "cholera"],
    "presha": ["hypertension"],
    "damu": ["cholera", "tuberculosis", "pregnancy", "diarrhea"],
    "ujauzito": ["pregnancy"],
    "mjamzito": ["pregnancy"],
    "mtoto": ["child_illness"],
    "watoto": ["child_illness"],
    "sukari": ["diabetes"],
    "kisukari": ["diabetes"],
    "ganzi": ["hypertension", "diabetes"],
    "uso": ["hypertension"],
    "macho": ["malaria", "diabetes", "hypertension"],
    "jasho": ["malaria", "diabetes", "tuberculosis"],
    "uchovu": ["malaria", "anemia", "diabetes", "tuberculosis"],
    "udhaifu": ["diarrhea", "cholera", "anemia"],
    "kuona kiza": ["dizziness", "hypertension", "anemia"],
    "kupoteza nguvu": ["dizziness", "dehydration", "anemia"],

    # English symptoms
    "fever": ["malaria", "typhoid", "pneumonia", "tuberculosis"],
    "headache": ["malaria", "typhoid", "hypertension", "dizziness"],
    "dizziness": ["hypertension", "diabetes", "dizziness", "anemia"],
    "dizzy": ["hypertension", "diabetes", "dizziness", "anemia"],
    "cough": ["pneumonia", "tuberculosis"],
    "breathing": ["pneumonia", "tuberculosis", "hypertension"],
    "diarrhea": ["cholera", "diarrhea", "typhoid"],
    "vomiting": ["cholera", "malaria", "pregnancy"],
    "stomach": ["typhoid", "diarrhea", "cholera"],
    "blood": ["cholera", "tuberculosis", "pregnancy", "diarrhea"],
    "pregnant": ["pregnancy"],
    "child": ["child_illness"],
    "baby": ["child_illness"],
    "sugar": ["diabetes"],
    "diabetes": ["diabetes"],
    "numb": ["hypertension", "diabetes"],
    "weakness": ["diarrhea", "cholera", "anemia", "dizziness"],
    "tired": ["malaria", "anemia", "diabetes", "tuberculosis"],
    "fatigue": ["malaria", "anemia", "diabetes", "tuberculosis"],
    "seeing dark": ["dizziness", "hypertension", "anemia"],
    "fainting": ["dizziness", "dehydration", "anemia"],
    "chills": ["malaria"],
    "sweating": ["malaria", "diabetes", "tuberculosis"],
}


def get_relevant_conditions(symptoms_text: str) -> list:
    """Get list of possibly relevant conditions based on symptom keywords."""
    text_lower = symptoms_text.lower()
    conditions = set()
    
    for keyword, condition_list in SYMPTOM_CONDITIONS.items():
        if keyword in text_lower:
            conditions.update(condition_list)
    
    return list(conditions)


def get_condition_info(condition: str, lang: str = "sw") -> dict:
    """Get information about a specific condition."""
    if condition in HEALTH_KNOWLEDGE:
        return HEALTH_KNOWLEDGE[condition]
    return None


def format_condition_response(condition: str, lang: str = "sw") -> str:
    """Format a brief response about a condition."""
    info = get_condition_info(condition, lang)
    if not info:
        return None
    
    name = info["names"].get(lang, info["names"]["sw"])
    desc = info["description"].get(lang, info["description"]["sw"])
    first_aid = info["first_aid"].get(lang, info["first_aid"]["sw"])
    
    if lang == "sw":
        response = f"{name}:\n{desc}\n\nMsaada wa kwanza:\n"
    else:
        response = f"{name}:\n{desc}\n\nFirst aid:\n"
    
    for i, step in enumerate(first_aid[:3], 1):
        response += f"{i}. {step}\n"
    
    return response
