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
    # Welcome screen and language selection
    "welcome_sw": (
        CON,
        "Karibu AfyaMkononi\n"
        "Msaada wa afya bila\ninternet\n\n"
        "Chagua lugha yako:\n"
        "1. Kiswahili\n"
        "2. English",
    ),
    
    "welcome_en": (
        CON,
        "Welcome to AfyaMkononi\n"
        "Health help, no internet\n\n"
        "Choose your language:\n"
        "1. Kiswahili\n"
        "2. English",
    ),

    # Main menu
    "main_sw": (
        CON,
        "Una tatizo gani leo?\n\n"
        "1. Homa au maumivu mwili\n"
        "2. Kikohozi au pumzi ngumu\n"
        "3. Kuhara au kutapika\n"
        "4. Kizunguzungu au shinikizo\n"
        "5. Dalili nyingine\n"
        "0. Toka",
    ),

    "main_en": (
        CON,
        "What is your problem today?\n\n"
        "1. Fever or body pain\n"
        "2. Cough or breathing problems\n"
        "3. Diarrhea or vomiting\n"
        "4. Dizziness or blood pressure\n"
        "5. Other symptoms\n"
        "0. Exit",
    ),

    # --- MALARIA ---
    "malaria_q1_sw": (
        CON,
        "HOMA\n\n"
        "Je, una homa inayokuja\nna kuondoka, baridi au\nkutetemeka mwili?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "malaria_q1_en": (
        CON,
        "FEVER\n\n"
        "Do you have fluctuating\nfever, chills, or\nshivering?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "malaria_q2_sw": (
        CON,
        "HOMA (HATARI)\n\n"
        "Je, unachanganyikiwa,\nmacho ni ya njano, au\nhuwezi kuamka kabisa?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "malaria_q2_en": (
        CON,
        "FEVER (DANGER)\n\n"
        "Are you confused,\nhave yellow eyes, or\nunable to wake up?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    # --- PNEUMONIA ---
    "pneumonia_q1_sw": (
        CON,
        "KIKOHOZI\n\n"
        "Je, unapumua haraka au\nkwa shida sana kuliko\nkawaida?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "pneumonia_q1_en": (
        CON,
        "COUGH\n\n"
        "Is your breathing\nfaster or much more\ndifficult than usual?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "pneumonia_q2_sw": (
        CON,
        "KIKOHOZI (HATARI)\n\n"
        "Je, mbavu zinaingia\nndani sana wakati wa\nkuvuta pumzi?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "pneumonia_q2_en": (
        CON,
        "COUGH (DANGER)\n\n"
        "Are the ribs pulling\nin deeply while\nbreathing?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    # --- DIARRHEA ---
    "diarrhea_q1_sw": (
        CON,
        "KUHARA\n\n"
        "Je, unaharisha maji\nmara 3 au zaidi leo?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "diarrhea_q1_en": (
        CON,
        "DIARRHEA\n\n"
        "Are you passing watery\nstool 3 or more\ntimes today?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "diarrhea_q2_sw": (
        CON,
        "KUHARA (HATARI)\n\n"
        "Je, macho yamezama,\nhauna mkojo, au kuna\ndamu kwenye choo?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "diarrhea_q2_en": (
        CON,
        "DIARRHEA (DANGER)\n\n"
        "Are eyes sunken,\nno urination, or\nblood in stool?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    # --- BLOOD PRESSURE (BP) ---
    "bp_q1_sw": (
        CON,
        "PRESHA (HATARI)\n\n"
        "Je, una ganzi, uso\nkulegea, au shida ya\nkuongea ghafla?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "bp_q1_en": (
        CON,
        "BP (DANGER)\n\n"
        "Do you have numbness,\nface drooping, or\nsudden speech trouble?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),

    "bp_q2_sw": (
        CON,
        "PRESHA\n\n"
        "Je, kichwa kinauma\nsana (kisogoni) au una\nkizunguzungu kikali?\n\n"
        "1. Ndiyo\n"
        "2. Hapana\n"
        "0. Rudi",
    ),

    "bp_q2_en": (
        CON,
        "BP\n\n"
        "Severe headache\n(at the back) or\nsevere dizziness?\n\n"
        "1. Yes\n"
        "2. No\n"
        "0. Back",
    ),
}

RESULTS = {
    # --- RED CATEGORY (RED) - Immediate help and Reassurance ---
    "red_malaria_sw": (
        END,
        "DHARURA - MALARIA KALI\n\n"
        "Dalili hizi ni hatari sana.\n"
        "Nenda hospitali SASA HIVI.\n"
        "Usisubiri hata dakika.\n"
        "Kila dakika inaokoa\nmaisha.",
    ),
    "red_pneumonia_sw": (
        END,
        "DHARURA - NIMONIA KALI\n\n"
        "Mgonjwa anahitaji oksijeni\nna dawa haraka sana.\n"
        "Nenda hospitali SASA HIVI.\n"
        "Msaidie kukaa wima\nnjiani.",
    ),
    "red_diarrhea_sw": (
        END,
        "DHARURA - UPUNGUFU WA MAJI\n\n"
        "Mwili umepoteza maji mengi.\nHali hii ni ya hatari.\n"
        "Nenda hospitali SASA.\n"
        "Mpe maji kidogo kidogo\nnjiani.",
    ),
    "red_bp_sw": (
        END,
        "DHARURA - DALILI ZA KIHARUSI\n\n"
        "Hizi ni dalili za ubongo.\n"
        "Nenda hospitali SASA HIVI.\n"
        "Omba msaada wa jirani.\n"
        "Usimkabidhi peke yake.",
    ),
    # --- YELLOW CATEGORY (YELLOW) - Advice and Testing today ---
    "yellow_malaria_sw": (
        END,
        "USHAURI: MALARIA\n\n"
        "Usijali, hali hii inatibika.\n"
        "1. Fika kituo cha afya leo\n"
        "   upate kipimo cha malaria\n"
        "2. Kunywa maji mengi\n"
        "3. Usitumie dawa bila\n"
        "   majibu ya daktari.",
    ),
    "yellow_pneumonia_sw": (
        END,
        "USHAURI: NIMONIA\n\n"
        "Pole sana, utapona.\n"
        "1. Fika kituoni leo\n"
        "2. Msaidie kukaa wima\n"
        "3. Hakikisha ana joto\n"
        "4. Usitumie dawa yoyote\n"
        "   kabla ya kupimwa.",
    ),
    "yellow_diarrhea_sw": (
        END,
        "USHAURI: KUHARA\n\n"
        "Usijali, utapata nafuu.\n"
        "1. Mpe ORS au maji ya\n"
        "   chumvi na sukari sasa\n"
        "2. Fika zahanati leo\n"
        "3. Mtoto azidi kunyonyeshwa.",
    ),
    "yellow_bp_sw": (
        END,
        "USHAURI: PRESHA\n\n"
        "Tulia na pumzika kwanza.\n"
        "1. Fika kituo cha afya leo\n"
        "   kupima shinikizo (BP)\n"
        "2. Usinywe dawa yoyote\n"
        "   bila vipimo sahihi\n"
        "3. Epuka chumvi na kelele.",
    ),
    # --- GREEN CATEGORY (GREEN) - Rest and Monitoring ---
    "green_sw": (
        END,
        "MAPUMZIKO\n\n"
        "Dalili hizi si za dharura.\n"
        "Pumzika na kunywa maji.\n"
        "Hali ikibadilika au\n"
        "ukijihisi vibaya zaidi,\n"
        "fika kituo cha afya.",
    ),
    # --- UNRECOGNIZED SYMPTOMS AND EXIT ---
    "other_sw": (
        END,
        "MSAADA ZAIDI\n\n"
        "Tafadhali fika zahanati\n"
        "kwa uchunguzi zaidi.\n"
        "Ni muhimu mgonjwa amuone\n"
        "daktari leo kwa usalama.",
    ),
    "exit_sw": (
        END,
        "Asante kwa kututumia.\n"
        "Tunakutakia afya njema.\n"
        "Piga *24929# wakati\n"
        "wowote ukihitaji msaada.",
    ),
    # English results
    "red_malaria_en": (
        END,
        "EMERGENCY - SEVERE MALARIA\n\n"
        "These signs are very\ndangerous. Go to\nhospital RIGHT NOW.\n"
        "Do not wait. Every\nminute matters.",
    ),
    "red_pneumonia_en": (
        END,
        "EMERGENCY - SEVERE PNEUMONIA\n\n"
        "Patient needs oxygen\nand medicine urgently.\n"
        "Go to hospital\nRIGHT NOW.",
    ),
    "red_diarrhea_en": (
        END,
        "EMERGENCY - DEHYDRATION\n\n"
        "Body has lost too much\nwater. Very dangerous.\n"
        "Go to hospital NOW.\n"
        "Give small water sips\non the way.",
    ),
    "red_bp_en": (
        END,
        "EMERGENCY - STROKE SIGNS\n\n"
        "These are brain emergency\nsigns. Go to hospital\nRIGHT NOW.\n"
        "Get a neighbour to help.\nDo not leave alone.",
    ),
    "yellow_malaria_en": (
        END,
        "ADVICE: POSSIBLE MALARIA\n\n"
        "Do not worry, this is\ntreatable.\n"
        "1. Visit clinic TODAY\n"
        "   for a blood test\n"
        "2. Drink plenty water\n"
        "3. No medicine before\n"
        "   seeing a doctor.",
    ),
    "yellow_pneumonia_en": (
        END,
        "ADVICE: POSSIBLE PNEUMONIA\n\n"
        "1. Visit clinic today\n"
        "2. Keep patient upright\n"
        "3. Keep them warm\n"
        "4. No medicine before\n"
        "   being examined.",
    ),
    "yellow_diarrhea_en": (
        END,
        "ADVICE: DIARRHEA\n\n"
        "1. Give ORS or sugar-salt\n"
        "   water right now\n"
        "2. Visit clinic today\n"
        "3. Keep breastfeeding\n"
        "   if infant.",
    ),
    "yellow_bp_en": (
        END,
        "ADVICE: BLOOD PRESSURE\n\n"
        "Rest and calm down first.\n"
        "1. Visit clinic today\n"
        "   to check BP\n"
        "2. No medicine without\n"
        "   proper tests\n"
        "3. Avoid salt and stress.",
    ),
    "green_en": (
        END,
        "REST AND MONITOR\n\n"
        "Symptoms are not\nserious right now.\n"
        "Rest and drink water.\n"
        "If you feel worse,\nvisit a health center.",
    ),
    "other_en": (
        END,
        "MORE HELP NEEDED\n\n"
        "Please visit the nearest\nhealth center for a\nproper check-up.\n"
        "It is important to\nsee a doctor today.",
    ),
    "exit_en": (
        END,
        "Thank you for using\nAfyaMkononi.\n"
        "We wish you good health.\n"
        "Dial *24929# anytime\nyou need help.",
    ),
}
