RED = "red"
YELLOW = "yellow"
GREEN = "green"

MALARIA = "malaria"
PNEUMONIA = "pneumonia"
DIARRHEA = "diarrhea"
BP = "bp"
OTHER = "other"

STEP_WELCOME = "welcome"
STEP_MAIN = "main"
STEP_Q1 = "q1"
STEP_Q2 = "q2"
STEP_RESULT = "result"

CON = "CON"
END = "END"

CHANNEL_USSD = "ussd"
CHANNEL_SMS = "sms"
CHANNEL_APP = "app"

LANG_SW = "sw"
LANG_EN = "en"


SCREENS = {
    # Welcome screen - simple and friendly
    "welcome_sw": (
        CON,
        "Karibu AfyaMkononi!\n\n"
        "Chagua lugha:\n"
        "1. Kiswahili\n"
        "2. English",
    ),
    
    "welcome_en": (
        CON,
        "Welcome to AfyaMkononi!\n\n"
        "Choose language:\n"
        "1. Kiswahili\n"
        "2. English",
    ),

    # Main menu - clear options
    "main_sw": (
        CON,
        "Una tatizo gani?\n\n"
        "1. Homa/Joto mwilini\n"
        "2. Kikohozi/Pumzi shida\n"
        "3. Kuhara/Kutapika\n"
        "4. Kizunguzungu/Presha\n"
        "5. Lingine\n\n"
        "0. Toka",
    ),

    "main_en": (
        CON,
        "What's your problem?\n\n"
        "1. Fever/Body heat\n"
        "2. Cough/Breathing\n"
        "3. Diarrhea/Vomiting\n"
        "4. Dizziness/BP\n"
        "5. Other\n\n"
        "0. Exit",
    ),

    # --- MALARIA/FEVER ---
    "malaria_q1_sw": (
        CON,
        "HOMA\n\n"
        "Una baridi au kutetemeka?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "malaria_q1_en": (
        CON,
        "FEVER\n\n"
        "Have chills or shivering?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "malaria_q2_sw": (
        CON,
        "HOMA - Maswali Zaidi\n\n"
        "Unachanganyikiwa au\nmacho ni ya njano?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "malaria_q2_en": (
        CON,
        "FEVER - More Questions\n\n"
        "Confused or yellow eyes?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    # --- PNEUMONIA/COUGH ---
    "pneumonia_q1_sw": (
        CON,
        "KIKOHOZI\n\n"
        "Pumzi ni ngumu kuliko\nkawaida?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "pneumonia_q1_en": (
        CON,
        "COUGH\n\n"
        "Breathing harder than\nnormal?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "pneumonia_q2_sw": (
        CON,
        "KIKOHOZI - Maswali Zaidi\n\n"
        "Mbavu zinaingia ndani\nukipumua?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "pneumonia_q2_en": (
        CON,
        "COUGH - More Questions\n\n"
        "Ribs pulling in when\nbreathing?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    # --- DIARRHEA ---
    "diarrhea_q1_sw": (
        CON,
        "KUHARA\n\n"
        "Unaenda haja kubwa maji\nmara 3+ leo?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "diarrhea_q1_en": (
        CON,
        "DIARRHEA\n\n"
        "Watery stool 3+ times\ntoday?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "diarrhea_q2_sw": (
        CON,
        "KUHARA - Maswali Zaidi\n\n"
        "Macho yamezama, hauna\nmkojo, au damu kwenye\nchoo?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "diarrhea_q2_en": (
        CON,
        "DIARRHEA - More Questions\n\n"
        "Sunken eyes, no urine,\nor blood in stool?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    # --- BLOOD PRESSURE ---
    "bp_q1_sw": (
        CON,
        "PRESHA\n\n"
        "Una ganzi, uso kulegea,\nau shida kuongea ghafla?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "bp_q1_en": (
        CON,
        "BP\n\n"
        "Numbness, face drooping,\nor sudden speech trouble?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "bp_q2_sw": (
        CON,
        "PRESHA - Maswali Zaidi\n\n"
        "Kichwa kinauma sana au\nkizunguzungu kikali?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "bp_q2_en": (
        CON,
        "BP - More Questions\n\n"
        "Severe headache or\ndizziness?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),
}

RESULTS = {
    # --- DHARURA (RED) - Hospitali SASA ---
    "red_malaria_sw": (
        END,
        "DHARURA!\n\n"
        "Dalili za malaria kali.\n"
        "Hospitali SASA!\n"
        "Usisubiri.",
    ),
    "red_pneumonia_sw": (
        END,
        "DHARURA!\n\n"
        "Dalili za nimonia kali.\n"
        "Hospitali SASA!\n"
        "Msaidie kukaa wima.",
    ),
    "red_diarrhea_sw": (
        END,
        "DHARURA!\n\n"
        "Mwili umekosa maji.\n"
        "Hospitali SASA!\n"
        "Mpe maji kidogo njiani.",
    ),
    "red_bp_sw": (
        END,
        "DHARURA!\n\n"
        "Dalili za kiharusi.\n"
        "Hospitali SASA!\n"
        "Omba msaada wa jirani.",
    ),
    
    # --- USHAURI (YELLOW) - Zahanati leo ---
    "yellow_malaria_sw": (
        END,
        "USHAURI - Malaria\n\n"
        "Fika zahanati leo upimwe.\n"
        "Kunywa maji mengi.\n"
        "Usitumie dawa bila kipimo.",
    ),
    "yellow_pneumonia_sw": (
        END,
        "USHAURI - Kikohozi\n\n"
        "Fika zahanati leo.\n"
        "Kaa wima, sio kulala.\n"
        "Hakikisha una joto.",
    ),
    "yellow_diarrhea_sw": (
        END,
        "USHAURI - Kuhara\n\n"
        "Mpe ORS au maji+chumvi+sukari.\n"
        "Fika zahanati leo.\n"
        "Mtoto aendelee kunyonya.",
    ),
    "yellow_bp_sw": (
        END,
        "USHAURI - Presha\n\n"
        "Pumzika kwanza.\n"
        "Fika zahanati kupima BP.\n"
        "Epuka chumvi na stress.",
    ),
    
    # --- MAPUMZIKO (GREEN) ---
    "green_sw": (
        END,
        "Poa, si dharura.\n\n"
        "Pumzika na kunywa maji.\n"
        "Ukijihisi vibaya zaidi,\n"
        "fika zahanati.",
    ),
    
    # --- EXIT na OTHER ---
    "other_sw": (
        END,
        "Fika zahanati leo\n"
        "kwa uchunguzi zaidi.\n"
        "Daktari atakusaidia.",
    ),
    "exit_sw": (
        END,
        "Asante!\n"
        "Tunakutakia afya njema.\n"
        "Piga *24929# ukihitaji.",
    ),
    
    # --- ENGLISH RESULTS ---
    "red_malaria_en": (
        END,
        "EMERGENCY!\n\n"
        "Severe malaria signs.\n"
        "Hospital NOW!\n"
        "Don't wait.",
    ),
    "red_pneumonia_en": (
        END,
        "EMERGENCY!\n\n"
        "Severe pneumonia signs.\n"
        "Hospital NOW!\n"
        "Keep patient upright.",
    ),
    "red_diarrhea_en": (
        END,
        "EMERGENCY!\n\n"
        "Severe dehydration.\n"
        "Hospital NOW!\n"
        "Give small water sips.",
    ),
    "red_bp_en": (
        END,
        "EMERGENCY!\n\n"
        "Stroke signs detected.\n"
        "Hospital NOW!\n"
        "Get help from neighbor.",
    ),
    "yellow_malaria_en": (
        END,
        "ADVICE - Fever\n\n"
        "Visit clinic today for test.\n"
        "Drink lots of water.\n"
        "No medicine without test.",
    ),
    "yellow_pneumonia_en": (
        END,
        "ADVICE - Cough\n\n"
        "Visit clinic today.\n"
        "Stay upright, not lying.\n"
        "Keep warm.",
    ),
    "yellow_diarrhea_en": (
        END,
        "ADVICE - Diarrhea\n\n"
        "Give ORS or water+salt+sugar.\n"
        "Visit clinic today.\n"
        "Keep breastfeeding baby.",
    ),
    "yellow_bp_en": (
        END,
        "ADVICE - BP\n\n"
        "Rest first.\n"
        "Visit clinic to check BP.\n"
        "Avoid salt and stress.",
    ),
    "green_en": (
        END,
        "Not urgent.\n\n"
        "Rest and drink water.\n"
        "If worse, visit clinic.",
    ),
    "other_en": (
        END,
        "Visit clinic today\n"
        "for proper check-up.\n"
        "Doctor will help.",
    ),
    "exit_en": (
        END,
        "Thank you!\n"
        "Stay healthy.\n"
        "Dial *24929# if needed.",
    ),
}
