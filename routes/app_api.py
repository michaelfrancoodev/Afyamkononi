from fastapi import APIRouter
from pydantic import BaseModel
from services.triage import triage
from services.ai_engine import ask_gemini
from services.health_data import get_disease

router = APIRouter()


class CheckRequest(BaseModel):
    phone:   str = ""
    disease: str
    q1:      str
    q2:      str = ""
    lang:    str = "sw"


class CheckResponse(BaseModel):
    disease:  str
    severity: str
    advice:   str
    go_now:   bool


@router.post("/check", response_model=CheckResponse)
async def app_check(req: CheckRequest):
    severity     = triage(req.disease, req.q1, req.q2 or None)
    disease_info = get_disease(req.disease)

    name_key      = f"name_{req.lang}"
    disease_name  = disease_info.get(name_key, req.disease)
    first_aid_key = f"first_aid_{req.lang}"
    first_aid     = disease_info.get(first_aid_key, "")

    if severity == "red":
        advice = (
            f"DHARURA! Nenda hospitali SASA. {first_aid}"
            if req.lang == "sw" else
            f"EMERGENCY! Go to hospital NOW. {first_aid}"
        )
    else:
        advice = await ask_gemini(f"{disease_name}: {first_aid}", req.lang)

    return CheckResponse(
        disease=req.disease,
        severity=severity,
        advice=advice,
        go_now=(severity == "red"),
    )
