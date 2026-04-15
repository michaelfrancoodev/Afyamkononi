import hashlib
from datetime import datetime, timezone
from database.client import get_client


def save_consultation(phone, channel, lang, disease, severity, advice_given) -> str | None:
    try:
        db  = get_client()
        row = {
            "phone_hash":   _hash_phone(phone),
            "channel":      channel,
            "lang":         lang,
            "disease":      disease,
            "severity":     severity,
            "advice_given": advice_given[:500],
            "created_at":   datetime.now(timezone.utc).isoformat(),
        }
        res = db.table("consultations").insert(row).execute()
        return res.data[0]["id"] if res.data else None
    except Exception:
        return None


def save_feedback(consultation_id: str, helpful: bool) -> bool:
    try:
        db = get_client()
        db.table("feedback").insert({
            "consultation_id": consultation_id,
            "helpful":         helpful,
            "created_at":      datetime.now(timezone.utc).isoformat(),
        }).execute()
        return True
    except Exception:
        return False


def get_stats() -> dict:
    try:
        db    = get_client()
        total = db.table("consultations").select("id", count="exact").execute()
        return {"total": total.count or 0}
    except Exception:
        return {"total": 0}


def _hash_phone(phone: str) -> str:
    return hashlib.sha256(phone.encode()).hexdigest()[:16]
