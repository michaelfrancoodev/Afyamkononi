from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime, timezone

router = APIRouter()


@router.get("/ping")
async def ping():
    return JSONResponse({
        "status": "ok",
        "service": "AfyaMkononi",
        "time": datetime.now(timezone.utc).isoformat()
    })


@router.get("/health")
async def health():
    return JSONResponse({"status": "ok"})
