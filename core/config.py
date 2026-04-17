import os
from dotenv import load_dotenv

load_dotenv()

# Africa's Talking
AT_API_KEY   = os.getenv("AT_API_KEY", "")
AT_USERNAME  = os.getenv("AT_USERNAME", "sandbox")
AT_SHORTCODE = os.getenv("AT_SHORTCODE", "*24929#")

# Google Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL   = "gemini-2.5-flash"

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "") or os.getenv("SUPABASE_SERVICE_ROLE_KEY", "") or os.getenv("SUPABASE_ANON_KEY", "")

# App settings
ENV      = os.getenv("ENV", "development")
IS_PROD  = ENV == "production"
DEBUG    = not IS_PROD

# Africa's Talking enforces a 182 character limit per USSD screen
USSD_CHAR_LIMIT = 182
