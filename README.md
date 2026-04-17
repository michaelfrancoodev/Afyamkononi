# AfyaMkononi

AI-powered health assistant accessible via USSD and SMS - no internet required.

**USSD Code: `*24929#`**

---

## Problem Statement

In rural Africa, millions of people live hours away from the nearest hospital. When a child develops severe malaria at midnight, or someone shows stroke symptoms, there is no doctor nearby, no internet access, and often no knowledge of what to do first.

## Solution

AfyaMkononi puts a health assistant in everyone's pocket - even on a basic phone without internet. Anyone can dial `*24929#` or send an SMS to check symptoms, receive first-aid guidance in their preferred language, and determine whether to seek immediate medical attention.

---

## How It Works

1. User dials `*24929#` on their phone
2. Selects preferred language
3. System asks targeted questions about symptoms
4. Based on responses, system provides triage result:
   - **RED** - Go to hospital NOW (emergency)
   - **YELLOW** - Visit health center today
   - **GREEN** - Rest at home and monitor

Each response includes actionable first-aid steps.

---

## Access Channels

| Channel | How to Use | Internet Required |
|---------|------------|-------------------|
| USSD | Dial `*24929#` | No |
| SMS | Send symptoms to shortcode | No |
| Mobile App | Flutter app (Phase 3) | Yes |

---

## Diseases Covered

| Disease | Danger Signs | Triage Action |
|---------|--------------|---------------|
| Malaria | Confusion, yellow eyes, unable to wake | Hospital NOW |
| Pneumonia | Chest indrawing when breathing, severe cough | Hospital NOW |
| Diarrhea/Cholera | Sunken eyes, no urine, blood in stool | Hospital NOW |
| Hypertension | One-sided numbness, facial drooping, stroke signs | Hospital NOW |

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python FastAPI |
| AI Engine | Google Gemini 2.5 Flash |
| Database | Supabase (PostgreSQL) |
| USSD/SMS Gateway | Africa's Talking |
| Hosting | Render.com |

---

## Project Structure

```
Afyamkononi/
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
│
├── core/
│   ├── config.py             # Environment configuration
│   ├── constants.py          # Application constants
│   └── languages.py          # Multi-language support
│
├── services/
│   ├── ai_engine.py          # Gemini AI integration
│   ├── triage.py             # Symptom analysis logic
│   ├── session.py            # USSD session management
│   ├── sms_parser.py         # SMS message parsing
│   └── health_data.py        # Health records management
│
├── routes/
│   ├── ussd.py               # USSD endpoint handler
│   ├── sms.py                # SMS endpoint handler
│   ├── health.py             # Health check endpoint
│   └── app_api.py            # Mobile app API
│
├── database/
│   ├── client.py             # Supabase client
│   ├── queries.py            # Database queries
│   └── schema.sql            # Database schema
│
└── tests/
    ├── test_triage.py        # Triage logic tests
    └── test_ussd.py          # USSD flow tests
```

---

## USSD Flow

```
*24929#
    │
    ▼
┌─────────────────────────┐
│  SELECT LANGUAGE        │
│  1. Option 1            │
│  2. Option 2            │
└─────────────────────────┘
    │
    ▼
┌─────────────────────────┐
│  MAIN MENU              │
│  1. Check Symptoms      │
│  2. First Aid Tips      │
│  3. Emergency Contacts  │
└─────────────────────────┘
    │
    ▼ (Option 1)
┌─────────────────────────┐
│  SYMPTOM QUESTIONS      │
│  Fever? (Yes/No)        │
│  Headache? (Yes/No)     │
│  Vomiting? (Yes/No)     │
└─────────────────────────┘
    │
    ▼
┌─────────────────────────┐
│  TRIAGE RESULT          │
│  Diagnosis + Severity   │
│  + First Aid Steps      │
└─────────────────────────┘
```

---

## Setup Instructions

### Prerequisites

- Python 3.11+
- Google Gemini API Key
- Supabase Account
- Africa's Talking Account

### 1. Clone Repository

```bash
git clone https://github.com/michaelfrancoodev/Afyamkononi.git
cd Afyamkononi
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Google Gemini AI
GEMINI_API_KEY=your_gemini_api_key

# Supabase Database
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_service_role_key

# Africa's Talking
AT_USERNAME=sandbox
AT_API_KEY=your_api_key
AT_SHORTCODE=*24929#
```

### 5. Setup Database

Run this SQL in Supabase SQL Editor:

```sql
-- Users table
CREATE TABLE IF NOT EXISTS users (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    preferred_language VARCHAR(10) DEFAULT 'en',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_interaction TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Sessions table
CREATE TABLE IF NOT EXISTS sessions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    session_id VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    state VARCHAR(50) DEFAULT 'LANGUAGE_SELECT',
    language VARCHAR(10) DEFAULT 'en',
    data JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Health records table
CREATE TABLE IF NOT EXISTS health_records (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    phone_number VARCHAR(20) NOT NULL,
    symptoms JSONB NOT NULL,
    diagnosis VARCHAR(100),
    severity VARCHAR(20),
    advice TEXT,
    channel VARCHAR(10) DEFAULT 'ussd',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_sessions_session_id ON sessions(session_id);
CREATE INDEX IF NOT EXISTS idx_sessions_phone ON sessions(phone_number);
CREATE INDEX IF NOT EXISTS idx_health_records_phone ON health_records(phone_number);
```

### 6. Run Locally

```bash
uvicorn main:app --reload --port 8000
```

### 7. Test Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Test USSD (initial dial)
curl -X POST http://localhost:8000/ussd \
  -d "sessionId=test1&serviceCode=*24929#&phoneNumber=+254712345678&text="

# Test SMS
curl -X POST http://localhost:8000/sms \
  -d "from=+254712345678&to=24929&text=I have fever and headache"
```

---

## Deployment to Render

### Step 1: Create Web Service

1. Go to [render.com](https://render.com)
2. Click **New +** > **Web Service**
3. Connect your GitHub repository
4. Configure:

| Setting | Value |
|---------|-------|
| Name | `afyamkononi` |
| Runtime | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

### Step 2: Add Environment Variables

| Key | Value |
|-----|-------|
| `GEMINI_API_KEY` | Your Gemini API key |
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_KEY` | Your Supabase service role key |
| `AT_USERNAME` | `sandbox` (or production username) |
| `AT_API_KEY` | Your Africa's Talking API key |

### Step 3: Deploy

Click **Create Web Service** and wait 2-5 minutes for deployment.

Your app will be live at: `https://afyamkononi.onrender.com`

---

## Africa's Talking Configuration

### USSD Setup

1. Go to [africastalking.com](https://africastalking.com) > Sandbox
2. Navigate to **USSD** > **Create Channel**
3. Configure:
   - Service Code: `*384*24929#` (sandbox format)
   - Callback URL: `https://afyamkononi.onrender.com/ussd`

### SMS Setup

1. Navigate to **SMS** > **Shortcodes**
2. Set Callback URL: `https://afyamkononi.onrender.com/sms`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/ussd` | USSD callback handler |
| POST | `/sms` | SMS callback handler |
| GET | `/api/records/{phone}` | Get health records |

---

## Triage Logic

The system uses a rule-based triage algorithm with AI enhancement:

### Severity Levels

| Level | Color | Action Required |
|-------|-------|-----------------|
| Critical | RED | Go to hospital immediately |
| Moderate | YELLOW | Visit health center today |
| Mild | GREEN | Rest at home, monitor symptoms |

### Danger Signs (Always RED)

- Confusion or unconsciousness
- Difficulty breathing
- Chest indrawing
- Unable to drink/eat
- Blood in stool/vomit
- Severe dehydration
- One-sided weakness (stroke signs)

---

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_triage.py -v
```

---

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | Yes | Google AI Studio API key |
| `SUPABASE_URL` | Yes | Supabase project URL |
| `SUPABASE_KEY` | Yes | Supabase service role key |
| `AT_USERNAME` | Yes | Africa's Talking username |
| `AT_API_KEY` | Yes | Africa's Talking API key |
| `AT_SHORTCODE` | No | USSD shortcode (default: *24929#) |

---

## Getting API Keys

### Gemini API Key
1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Click **Create API Key**
3. Copy the key (starts with `AIzaSy`)

### Supabase Credentials
1. Go to [supabase.com](https://supabase.com)
2. Create/open your project
3. Go to **Settings** > **API**
4. Copy **Project URL** and **service_role** key

### Africa's Talking API Key
1. Go to [africastalking.com](https://africastalking.com)
2. Create account and go to Sandbox
3. Go to **Settings** > **API Key**
4. Generate and copy the key

---

## Safety Rules

1. **No medications** - System never recommends specific drugs
2. **No definitive diagnosis** - Always uses "may indicate" or "symptoms suggest"
3. **Always referral** - Every response ends with "Visit the nearest health facility"
4. **Privacy** - Phone numbers stored securely

---

## Database Schema

```sql
-- Users table
users (
  id                  UUID PRIMARY KEY,
  phone_number        VARCHAR(20) UNIQUE,
  preferred_language  VARCHAR(10),
  created_at          TIMESTAMPTZ,
  last_interaction    TIMESTAMPTZ
)

-- Sessions table
sessions (
  id            UUID PRIMARY KEY,
  session_id    VARCHAR(100) UNIQUE,
  phone_number  VARCHAR(20),
  state         VARCHAR(50),
  language      VARCHAR(10),
  data          JSONB,
  created_at    TIMESTAMPTZ,
  updated_at    TIMESTAMPTZ
)

-- Health records table
health_records (
  id            UUID PRIMARY KEY,
  phone_number  VARCHAR(20),
  symptoms      JSONB,
  diagnosis     VARCHAR(100),
  severity      VARCHAR(20),
  advice        TEXT,
  channel       VARCHAR(10),
  created_at    TIMESTAMPTZ
)
```

---

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m "Add new feature"`
4. Push to branch: `git push origin feature/new-feature`
5. Open a Pull Request

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## SDG Alignment

This project supports **UN Sustainable Development Goal 3: Good Health and Well-Being** by providing accessible health guidance to underserved communities in Africa.

---

## Contact

- GitHub: [@michaelfrancoodev](https://github.com/michaelfrancoodev)
- Project: [Afyamkononi](https://github.com/michaelfrancoodev/Afyamkononi)
