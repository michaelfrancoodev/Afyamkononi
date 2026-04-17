"""
AfyaMkononi v3.0 - SMS Health Assistant
Production-ready AI health advisor for East Africa
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.sms     import router as sms_router
from routes.app_api import router as app_router
from routes.health  import router as health_router

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AfyaMkononi",
    description="AI health assistant for East Africa via SMS - Accurate, Conversational, Helpful",
    version="3.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# SMS only - USSD removed
app.include_router(health_router)
app.include_router(sms_router)
app.include_router(app_router)


@app.on_event("startup")
async def startup_event():
    logger.info("AfyaMkononi v3.0 - SMS Health Assistant started")


@app.get("/")
async def root():
    return {
        "service": "AfyaMkononi",
        "version": "3.0.0",
        "channel": "sms",
        "description": "AI Health Assistant for East Africa",
        "docs": "/docs",
    }
