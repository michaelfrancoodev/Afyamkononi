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
        "MSAADA WA HARAKA\n\n"
        "Usijali, wahi kituo cha\n"
        "afya sasa upate msaada.\n"
        "Dalili hizi zinahitaji\n"
        "ushauri wa daktari\n"
        "mapema iwezekanavyo.",
    ),
    "red_pneumonia_sw": (
        END,
        "MSAADA WA HARAKA\n\n"
        "Usihofu, wahi hospitali\n"
        "upate msaada wa haraka.\n"
        "Msaidie mgonjwa kukaa\n"
        "wima (ameegama) ili\n"
        "apumue kwa urahisi.",
    ),
    "red_diarrhea_sw": (
        END,
        "MSAADA WA HARAKA\n\n"
        "Usijali, mwili unahitaji\n"
        "maji. Wahi kituo cha\n"
        "afya mapema kwa msaada.\n"
        "Mpe maji kidogo kidogo\n"
        "wakati mkiwa njiani.",
    ),
    "red_bp_sw": (
        END,
        "MSAADA WA HARAKA\n\n"
        "Usijali, tulia na msaidie\n"
        "mgonjwa kukaa wima.\n"
        "Wahi kituo cha afya sasa.\n"
        "Omba msaada wa jirani\n"
        "mgonjwa asikae peke yake.",
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
}
