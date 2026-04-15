# Severity levels returned by the triage engine
RED    = "red"      # go to hospital now
YELLOW = "yellow"   # visit clinic today
GREEN  = "green"    # rest at home, monitor

# Disease codes
MALARIA   = "malaria"
PNEUMONIA = "pneumonia"
DIARRHEA  = "diarrhea"
BP        = "bp"
OTHER     = "other"

# USSD session steps
STEP_WELCOME = "welcome"
STEP_MAIN    = "main"
STEP_Q1      = "q1"
STEP_Q2      = "q2"
STEP_RESULT  = "result"

# Africa's Talking response types
CON = "CON"  # session continues
END = "END"  # session ends

# Channels
CHANNEL_USSD = "ussd"
CHANNEL_SMS  = "sms"
CHANNEL_APP  = "app"

# Languages
LANG_SW = "sw"
LANG_EN = "en"


# All USSD screens. Every string is kept under 182 characters.
SCREENS = {
    "welcome_sw": (CON,
        "Karibu AfyaMkononi\n"
        "Huduma ya afya bila\ninternet\n\n"
        "Chagua lugha:\n"
        "1. Kiswahili\n"
        "2. English"
    ),
    "welcome_en": (CON,
        "Welcome to AfyaMkononi\n"
        "Health help, no internet\n\n"
        "Choose language:\n"
        "1. Kiswahili\n"
        "2. English"
    ),
    "main_sw": (CON,
        "Una tatizo gani?\n\n"
        "1. Homa/Maumivu\n"
        "2. Kikohozi/Pumzi\n"
        "3. Kuhara/Kutapika\n"
        "4. Kizunguzungu/BP\n"
        "5. Dalili nyingine\n"
        "0. Ondoka"
    ),
    "main_en": (CON,
        "What is your issue?\n\n"
        "1. Fever/Body pain\n"
        "2. Cough/Breathing\n"
        "3. Diarrhea/Vomiting\n"
        "4. Dizziness/BP\n"
        "5. Other symptoms\n"
        "0. Exit"
    ),

    # Malaria questions
    "malaria_q1_sw": (CON,
        "HOMA\n\n"
        "Je, una homa kali na\nunapotemeka au una\nbaridi kali?\n\n"
        "1. Ndiyo\n2. Hapana\n0. Rudi"
    ),
    "malaria_q1_en": (CON,
        "FEVER\n\n"
        "Do you have high fever\nwith shaking or chills?\n\n"
        "1. Yes\n2. No\n0. Back"
    ),
    "malaria_q2_sw": (CON,
        "HOMA\n\n"
        "Je, unachanganyikiwa,\nhuwezi kuamka, au\nmacho ni ya njano?\n\n"
        "1. Ndiyo\n2. Hapana\n0. Rudi"
    ),
    "malaria_q2_en": (CON,
        "FEVER\n\n"
        "Confused, cannot wake,\nor eyes are yellow?\n\n"
        "1. Yes\n2. No\n0. Back"
    ),

    # Pneumonia questions
    "pneumonia_q1_sw": (CON,
        "KIKOHOZI\n\n"
        "Je, anapumua kwa shida\nau kwa haraka kubwa?\n\n"
        "1. Ndiyo\n2. Hapana\n0. Rudi"
    ),
    "pneumonia_q1_en": (CON,
        "COUGH\n\n"
        "Is breathing very hard\nor extremely fast?\n\n"
        "1. Yes\n2. No\n0. Back"
    ),
    "pneumonia_q2_sw": (CON,
        "KIKOHOZI\n\n"
        "Angalia kifua:\nje, mbavu zinaingia\nndani anapovuta pumzi?\n\n"
        "1. Ndiyo\n2. Hapana\n0. Rudi"
    ),
    "pneumonia_q2_en": (CON,
        "COUGH\n\n"
        "Check the chest:\nribs visible when\nbreathing in?\n\n"
        "1. Yes\n2. No\n0. Back"
    ),

    # Diarrhea questions
    "diarrhea_q1_sw": (CON,
        "KUHARA\n\n"
        "Je, kuhara ni majimaji\nmengi na mara kwa mara?\n\n"
        "1. Ndiyo\n2. Hapana\n0. Rudi"
    ),
    "diarrhea_q1_en": (CON,
        "DIARRHEA\n\n"
        "Is it very watery and\nhappening very often?\n\n"
        "1. Yes\n2. No\n0. Back"
    ),
    "diarrhea_q2_sw": (CON,
        "KUHARA\n\n"
        "Macho yamezama, mdomo\nmkavu, au hakojoi kwa\nmuda mrefu?\n\n"
        "1. Ndiyo\n2. Hapana\n0. Rudi"
    ),
    "diarrhea_q2_en": (CON,
        "DIARRHEA\n\n"
        "Sunken eyes, dry mouth,\nor not urinating?\n\n"
        "1. Yes\n2. No\n0. Back"
    ),

    # Blood pressure question (only one question needed)
    "bp_q1_sw": (CON,
        "SHINIKIZO LA DAMU\n\n"
        "Je, una ganzi upande\nmmoja, uso unalegea,\nau huwezi kuongea?\n\n"
        "1. Ndiyo\n2. Hapana\n0. Rudi"
    ),
    "bp_q1_en": (CON,
        "BLOOD PRESSURE\n\n"
        "Numbness on one side,\nface drooping, or cannot\nspeak normally?\n\n"
        "1. Yes\n2. No\n0. Back"
    ),
}


# Result screens shown at the end of each flow
RESULTS = {
    # RED results - go to hospital immediately
    "red_malaria_sw": (END,
        "!! DHARURA !!\n\n"
        "MALARIA KALI.\n"
        "Nenda hospitali SASA.\n"
        "Usisubiri asubuhi.\n"
        "Kila dakika ni muhimu\nkuokoa maisha."
    ),
    "red_pneumonia_sw": (END,
        "!! DHARURA !!\n\n"
        "NIMONIA KALI.\n"
        "Mpeleke hospitali SASA.\n"
        "Anahitaji oksijeni na\ndawa haraka sana."
    ),
    "red_diarrhea_sw": (END,
        "!! DHARURA !!\n\n"
        "UPUNGUFU WA MAJI.\n"
        "Nenda hospitali SASA.\n"
        "Mpe maji kidogo kidogo\nnjiani hadi hospitali."
    ),
    "red_bp_sw": (END,
        "!! DHARURA !!\n\n"
        "DALILI ZA KIHARUSI!\n"
        "Nenda hospitali SASA.\n"
        "Omba msaada wa jirani.\n"
        "Kila sekunde ni muhimu."
    ),
    "red_malaria_en": (END,
        "!! EMERGENCY !!\n\n"
        "SEVERE MALARIA.\n"
        "Go to hospital NOW.\n"
        "Do not wait. Every\nminute matters to\nsave this life."
    ),
    "red_pneumonia_en": (END,
        "!! EMERGENCY !!\n\n"
        "SEVERE PNEUMONIA.\n"
        "Go to hospital NOW.\n"
        "Patient needs oxygen\nand medicine urgently."
    ),
    "red_diarrhea_en": (END,
        "!! EMERGENCY !!\n\n"
        "SEVERE DEHYDRATION.\n"
        "Go to hospital NOW.\n"
        "Give small sips of\nwater on the way."
    ),
    "red_bp_en": (END,
        "!! EMERGENCY !!\n\n"
        "STROKE SIGNS!\n"
        "Go to hospital NOW.\n"
        "Ask someone to help.\n"
        "Every second counts."
    ),

    # YELLOW results - visit clinic today
    "yellow_malaria_sw": (END,
        "USHAURI - MALARIA\n\n"
        "Dalili zinaashiria\nMalaria. Hatua:\n"
        "* Pata kipimo leo\n"
        "* Kunywa maji mengi\n"
        "* Usitumie dawa bila\n  kipimo cha daktari"
    ),
    "yellow_pneumonia_sw": (END,
        "USHAURI - NIMONIA\n\n"
        "Inaweza kuwa Nimonia.\nHatua:\n"
        "* Fika kituoni leo\n"
        "* Mweke joto mtoto\n"
        "* Mpe maji mengi\n"
        "* Pumzika vizuri"
    ),
    "yellow_diarrhea_sw": (END,
        "HATUA ZA KWANZA\n\n"
        "Tengeneza ORS sasa:\n"
        "Maji 1L + vijiko 6\nsukari + 0.5 kijiko\nchumvi. Mpe kidogo\nkidogo. Fika zahanati."
    ),
    "yellow_bp_sw": (END,
        "USHAURI - SHINIKIZO\n\n"
        "Inaweza kuwa BP.\nHatua:\n"
        "* Pima BP kituoni\n  mapema\n"
        "* Pumzika sasa\n"
        "* Punguza chumvi\n"
        "* Epuka msongo"
    ),
    "yellow_malaria_en": (END,
        "ADVICE - MALARIA\n\n"
        "Symptoms suggest\nMalaria. Steps:\n"
        "* Get a blood test today\n"
        "* Drink lots of water\n"
        "* No medicine without\n  a proper test first"
    ),
    "yellow_pneumonia_en": (END,
        "ADVICE - PNEUMONIA\n\n"
        "Could be Pneumonia.\nSteps:\n"
        "* Visit clinic today\n"
        "* Keep patient warm\n"
        "* Give plenty fluids"
    ),
    "yellow_diarrhea_en": (END,
        "FIRST AID - ORS\n\n"
        "Make ORS now:\n"
        "1L water + 6 tsp sugar\n+ 0.5 tsp salt.\n"
        "Give small sips.\n"
        "Visit health center today."
    ),
    "yellow_bp_en": (END,
        "ADVICE - BLOOD PRESSURE\n\n"
        "Could be high BP.\nSteps:\n"
        "* Check BP at clinic soon\n"
        "* Rest now\n"
        "* Reduce salt\n"
        "* Avoid stress"
    ),

    # GREEN results - mild, rest and monitor
    "green_sw": (END,
        "USHAURI\n\n"
        "Dalili si kali sana.\n"
        "* Pumzika vizuri\n"
        "* Kunywa maji mengi\n"
        "* Kama hali itazidi\n"
        "  ndani ya siku 2,\n"
        "  fika kituo cha afya"
    ),
    "green_en": (END,
        "ADVICE\n\n"
        "Symptoms appear mild.\n"
        "* Rest well\n"
        "* Drink plenty water\n"
        "* If no improvement\n"
        "  in 2 days, visit the\n"
        "  nearest health center"
    ),

    # Unknown symptoms
    "other_sw": (END,
        "USHAURI\n\n"
        "Dalili hizi hazitambuliwi\nna mfumo wetu.\n\n"
        "Kwa usalama wako,\ntafadhali fika kituo\ncha afya kilicho\nkaribu nawe sasa."
    ),
    "other_en": (END,
        "ADVICE\n\n"
        "We could not identify\nthose symptoms.\n\n"
        "For your safety,\nplease visit the\nnearest health center\nright away."
    ),

    # Exit messages
    "exit_sw": (END,
        "Asante kwa kutumia\nAfyaMkononi.\n"
        "Piga *2392# tena\nupohitaji msaada."
    ),
    "exit_en": (END,
        "Thank you for using\nAfyaMkononi.\n"
        "Dial *2392# again\nwhenever you need help."
    ),
}
