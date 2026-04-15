# AfyaMkononi

AI-powered health assistant for rural Africa. Works on any phone, no internet needed.

**USSD code: `*2392#`**

---

## The Problem

In rural Africa, millions of people live hours from the nearest hospital. When a child gets severe malaria at midnight, or a mother shows signs of a stroke, there is no doctor nearby, no internet, and often no idea what to do first.

## What It Does

AfyaMkononi puts a health assistant in everyone's pocket - even a basic phone with no internet. Anyone can dial `*2392#` or send an SMS to check their symptoms, get clear first-aid guidance in Swahili or English, and know whether they need to go to hospital immediately.

## Channels

| Channel | How to use | Internet needed |
|---------|-----------|-----------------|
| USSD | Dial `*2392#` | No |
| SMS | Text symptoms to shortcode | No |
| App | Flutter mobile app | Optional |

## Diseases Covered

| Disease | Emergency Signs | Response |
|---------|----------------|----------|
| Malaria | Confusion + yellow eyes | Go to hospital NOW |
| Pneumonia | Ribs visible when breathing | Go to hospital NOW |
| Diarrhea | Sunken eyes + not urinating | Go to hospital NOW |
| Blood Pressure | Numbness on one side | Go to hospital NOW |

All other cases get first-aid steps and advice to visit the nearest clinic.

## Tech Stack

- **Backend**: Python + FastAPI
- **USSD and SMS**: Africa's Talking
- **AI**: Google Gemini 2.0 Flash (for SMS free-text replies)
- **Database**: Supabase
- **Hosting**: Render.com
- **App**: Flutter (phase 3)

Total cost: $0 - all free tiers.

## Project Structure

```
afyamkononi/
├── main.py
├── core/
│   ├── config.py          - environment variables
│   ├── constants.py       - USSD screens, severity levels
│   └── languages.py       - Swahili/English routing
├── services/
│   ├── triage.py          - RED/YELLOW/GREEN logic
│   ├── health_data.py     - disease knowledge base
│   ├── session.py         - USSD session state
│   ├── ai_engine.py       - Gemini integration
│   └── sms_parser.py      - SMS classifier
├── routes/
│   ├── ussd.py            - POST /ussd
│   ├── sms.py             - POST /sms
│   ├── app_api.py         - POST /check
│   └── health.py          - GET /ping
├── database/
│   ├── client.py          - Supabase connection
│   ├── queries.py         - database operations
│   └── schema.sql         - table definitions (run once)
└── tests/
    ├── test_ussd.py
    └── test_triage.py
```

## Setup

### 1. Get API keys

- Africa's Talking: [africastalking.com](https://africastalking.com) - register, go to sandbox, copy API key
- Gemini: [aistudio.google.com](https://aistudio.google.com) - click "Get API key"
- Supabase: [supabase.com](https://supabase.com) - new project, get URL and anon key

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment

```bash
cp .env.example .env
```

Open `.env` and fill in your keys.

### 4. Set up the database

1. Open your Supabase project
2. Go to SQL Editor
3. Paste the contents of `database/schema.sql` and run it

### 5. Run locally

```bash
uvicorn main:app --reload
```

API docs available at `http://localhost:8000/docs`

### 6. Test manually

```bash
curl -X POST http://localhost:8000/ussd \
  -d "sessionId=test1&phoneNumber=+255700000001&text=&serviceCode=*2392#"
```

### 7. Run tests

```bash
pytest tests/ -v
```

### 8. Deploy to Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a new Web Service
3. Connect your GitHub repo
4. Add all environment variables from your `.env` file
5. Render will deploy automatically

### 9. Connect Africa's Talking

1. In the AT dashboard, go to USSD and create a new channel
2. Set the callback URL to `https://your-app.onrender.com/ussd`
3. For SMS, set callback URL to `https://your-app.onrender.com/sms`

## USSD Flow

```
*2392#
└── Choose language
    └── Choose symptom category
        ├── Fever/Pain       Q1 -> Q2 -> result
        ├── Cough/Breathing  Q1 -> Q2 -> result
        ├── Diarrhea         Q1 -> Q2 -> result
        ├── Dizziness/BP     Q1       -> result
        └── Other            safety message -> visit clinic
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/ping` | Health check |
| POST | `/ussd` | USSD handler |
| POST | `/sms` | SMS handler |
| POST | `/check` | App JSON API |
| GET | `/docs` | API documentation |

## Important Notes

- AfyaMkononi is a first-aid guidance tool, not a replacement for doctors
- It never prescribes medicine by name
- It never diagnoses with certainty
- Every response ends with a referral to the nearest health center
- Phone numbers are hashed before storage

## SDG Alignment

This project addresses UN SDG 3 (Good Health and Well-being) by reducing preventable deaths from delayed treatment in rural communities using infrastructure that already exists - any mobile network.
