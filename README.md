# AfyaMkononi

Msaidizi wa afya kwa simu yoyote, bila internet. Health assistant for any phone, no internet needed.

**USSD: `*24929#`**

---

## Tatizo / The Problem

Maeneo ya vijijini Afrika, watu wanaishi mbali na hospitali. Wakati mtoto ana malaria kali usiku, au mtu anaonyesha dalili za kiharusi, hawana daktari, hawana internet, na mara nyingi hawajui hatua za kwanza za kufanya.

In rural Africa, millions live hours from the nearest hospital. When a child gets severe malaria at midnight, or someone shows stroke signs, there is no doctor nearby, no internet, and often no idea what to do first.

## Suluhisho / Solution

AfyaMkononi inaweka msaidizi wa afya mfukoni mwa kila mtu - hata simu ya kawaida bila internet. Mtu yeyote anaweza kupiga `*24929#` au kutuma SMS kuangalia dalili zake, kupata ushauri wa kwanza wa afya kwa Kiswahili au Kiingereza, na kujua kama anahitaji kwenda hospitali mara moja.

AfyaMkononi puts a health assistant in everyone's pocket - even a basic phone with no internet. Anyone can dial `*24929#` or send an SMS to check symptoms, get first-aid guidance in Swahili or English, and know whether to go to hospital immediately.

---

## Jinsi Inavyofanya Kazi / How It Works

1. Mtumiaji anapiga `*24929#` kwenye simu yake
2. Mfumo unauliza maswali mawili kuhusu dalili
3. Kulingana na majibu, mfumo unatoa matokeo:
   - **NYEKUNDU (RED)** - Nenda hospitali SASA HIVI
   - **NJANO (YELLOW)** - Fika kituoni leo
   - **KIJANI (GREEN)** - Pumzika nyumbani na angalia

Kila jibu lina hatua za kwanza za kufanya.

---

## Njia za Kufikia / Channels

| Njia | Jinsi ya Kutumia | Internet |
|------|------------------|----------|
| USSD | Piga `*24929#` | Hapana |
| SMS | Tuma dalili kwa shortcode | Hapana |
| App | Flutter mobile app (baadaye) | Ndiyo |

---

## Magonjwa Yanayoshughulikiwa / Diseases Covered

| Ugonjwa | Dalili za Hatari | Hatua |
|---------|------------------|-------|
| Malaria | Kuchanganyikiwa, macho ya njano | Hospitali SASA |
| Nimonia | Mbavu zinaingia ndani wakati wa kupumua | Hospitali SASA |
| Kuhara | Macho yamezama, hakuna mkojo | Hospitali SASA |
| Presha | Ganzi upande mmoja, uso kulegea | Hospitali SASA |

Dalili zisizotambulika zinaelekezwa moja kwa moja kwenda kliniki.

---

## Muundo wa Code / Project Structure

```
afyamkononi/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── render.yaml            # Render.com deployment config
├── .env.example           # Environment variables template
│
├── core/
│   ├── config.py          # API keys na settings
│   ├── constants.py       # USSD screens, severity levels
│   └── languages.py       # Swahili/English routing
│
├── services/
│   ├── triage.py          # RED/YELLOW/GREEN logic
│   ├── health_data.py     # Disease knowledge base
│   ├── session.py         # USSD session state management
│   ├── ai_engine.py       # Google Gemini integration
│   └── sms_parser.py      # SMS symptom classifier
│
├── routes/
│   ├── ussd.py            # POST /ussd - USSD handler
│   ├── sms.py             # POST /sms - SMS handler
│   ├── app_api.py         # POST /check - Mobile app API
│   └── health.py          # GET /ping, /health
│
├── database/
│   ├── client.py          # Supabase connection
│   ├── queries.py         # Database operations
│   └── schema.sql         # Table definitions
│
└── tests/
    ├── test_triage.py     # Triage logic tests
    └── test_ussd.py       # USSD flow integration tests
```

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python 3.11 + FastAPI |
| USSD/SMS | Africa's Talking |
| AI | Google Gemini 2.5 Flash |
| Database | Supabase (PostgreSQL) |
| Hosting | Render.com |
| Mobile App | Flutter (Phase 3) |

**Gharama: $0** - Huduma zote zina free tier.

---

## Kuanzisha / Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/afyamkononi.git
cd afyamkononi
```

### 2. Pata API Keys / Get API Keys

| Service | URL | Jinsi |
|---------|-----|-------|
| Africa's Talking | [africastalking.com](https://africastalking.com) | Register, go to Sandbox, copy API key |
| Google Gemini | [aistudio.google.com](https://aistudio.google.com) | Click "Get API key" |
| Supabase | [supabase.com](https://supabase.com) | New project, get URL and anon key |

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Fungua `.env` na ujaze keys zako:

```env
# Africa's Talking
AT_API_KEY=your_api_key_here
AT_USERNAME=sandbox
AT_SHORTCODE=*24929#

# Google Gemini
GEMINI_API_KEY=your_gemini_key_here

# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_or_service_key

# Environment
ENV=development
```

### 5. Setup Database

1. Fungua Supabase project yako
2. Nenda SQL Editor
3. Copy na paste contents za `database/schema.sql`
4. Run query

### 6. Run Locally

```bash
uvicorn main:app --reload --port 8000
```

API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### 7. Test Manually

```bash
# Welcome screen
curl -X POST http://localhost:8000/ussd \
  -d "sessionId=test1&phoneNumber=+255700000001&text=&serviceCode=*24929#"

# Full flow: Swahili -> Malaria -> Q1=Yes -> Q2=Yes (RED result)
curl -X POST http://localhost:8000/ussd \
  -d "sessionId=test2&phoneNumber=+255700000001&text=1*1*1*1&serviceCode=*24929#"
```

### 8. Run Tests

```bash
pytest tests/ -v
```

---

## Deployment to Render.com

### 1. Push to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Create Render Web Service

1. Nenda [render.com](https://render.com)
2. Click "New Web Service"
3. Connect GitHub repository
4. Render itasoma `render.yaml` automatically

### 3. Add Environment Variables

Kwenye Render dashboard, ongeza environment variables zote kutoka `.env` file yako.

### 4. Connect Africa's Talking

1. Kwenye AT dashboard, nenda USSD section
2. Create new USSD channel
3. Set callback URL: `https://your-app.onrender.com/ussd`
4. Kwa SMS, set callback: `https://your-app.onrender.com/sms`

**Muhimu:** Africa's Talking Sandbox inahitaji server iwe online wakati wote. Tumia [UptimeRobot](https://uptimerobot.com) kupiga `/ping` kila dakika 5 kuzuia server kulala.

---

## API Endpoints

| Method | Path | Maelezo |
|--------|------|---------|
| GET | `/` | Service info |
| GET | `/ping` | Health check (for uptime monitoring) |
| GET | `/health` | Health status |
| GET | `/docs` | Swagger API documentation |
| POST | `/ussd` | Africa's Talking USSD callback |
| POST | `/sms` | Africa's Talking SMS callback |
| POST | `/check` | Mobile app JSON API |

---

## USSD Flow

```
*24929#
└── Chagua lugha / Choose language
    ├── 1. Kiswahili
    └── 2. English
        └── Chagua tatizo / Choose problem
            ├── 1. Homa/Fever      → Q1 → Q2 → Result
            ├── 2. Kikohozi/Cough  → Q1 → Q2 → Result
            ├── 3. Kuhara/Diarrhea → Q1 → Q2 → Result
            ├── 4. Presha/BP       → Q1 → (Q2) → Result
            ├── 5. Nyingine/Other  → Visit clinic message
            └── 0. Toka/Exit
```

---

## Triage Logic

### Malaria
- Q1: Homa inayokuja na kuondoka, baridi, kutetemeka?
- Q2: Kuchanganyikiwa, macho ya njano, huwezi kuamka?
- **RED**: Q1=Yes AND Q2=Yes
- **YELLOW**: Q1=Yes AND Q2=No
- **GREEN**: Q1=No

### Nimonia (Pneumonia)
- Q1: Kupumua haraka au kwa shida sana?
- Q2: Mbavu zinaingia ndani sana wakati wa kuvuta pumzi?
- **RED**: Q1=Yes AND Q2=Yes
- **YELLOW**: Q1=Yes AND Q2=No
- **GREEN**: Q1=No

### Kuhara (Diarrhea)
- Q1: Choo cha majimaji mara 3+ leo?
- Q2: Macho yamezama, hakuna mkojo, damu kwenye choo?
- **RED**: Q1=Yes AND Q2=Yes
- **YELLOW**: Q1=Yes AND Q2=No
- **GREEN**: Q1=No

### Presha (Blood Pressure)
- Q1: Ganzi, uso kulegea, shida ya kuongea ghafla? (Dalili za kiharusi)
- Q2: Kichwa kinauma sana (kisogoni) au kizunguzungu kikali?
- **RED**: Q1=Yes (stroke signs - emergency immediately)
- **YELLOW**: Q1=No AND Q2=Yes
- **GREEN**: Q1=No AND Q2=No

---

## Kanuni za Usalama / Safety Rules

1. **Hakuna dawa** - Mfumo hautaji jina la dawa yoyote
2. **Hakuna diagnosis ya uhakika** - Daima tunasema "inaweza kuwa" au "dalili zinaashiria"
3. **Daima referral** - Kila jibu linaishia na "Fika kituo cha afya kilicho karibu nawe"
4. **Privacy** - Nambari za simu zinahifadhiwa kama SHA256 hash tu, si wazi

---

## Database Schema

```sql
-- Consultations table
consultations (
  id           UUID PRIMARY KEY,
  phone_hash   TEXT,      -- SHA256 hash of phone number
  channel      TEXT,      -- ussd | sms | app
  lang         TEXT,      -- sw | en
  disease      TEXT,      -- malaria | pneumonia | diarrhea | bp | other
  severity     TEXT,      -- red | yellow | green
  advice_given TEXT,
  created_at   TIMESTAMPTZ
)

-- Feedback table
feedback (
  id                UUID PRIMARY KEY,
  consultation_id   UUID REFERENCES consultations,
  helpful           BOOLEAN,
  created_at        TIMESTAMPTZ
)
```

---

## SDG Alignment

Mradi huu unashughulikia **UN SDG 3 - Good Health and Well-being** kwa kufikia watu wa vijijini ambao hawana upatikanaji wa huduma za afya kupitia miundombinu iliyopo tayari ya simu za kawaida.

This project addresses **UN SDG 3 - Good Health and Well-being** by reaching rural communities without healthcare access through existing basic mobile infrastructure.

---

## License

MIT License

---

## Contact

For questions or contributions, open an issue on GitHub.
