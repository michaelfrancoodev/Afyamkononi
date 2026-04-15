from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.ussd    import router as ussd_router
from routes.sms     import router as sms_router
from routes.app_api import router as app_router
from routes.health  import router as health_router

app = FastAPI(
    title="AfyaMkononi",
    description="AI health assistant for rural Africa - USSD, SMS, and Mobile",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(ussd_router)
app.include_router(sms_router)
app.include_router(app_router)


@app.get("/")
async def root():
    return {
        "service": "AfyaMkononi",
        "ussd": "*2392#",
        "channels": ["ussd", "sms", "app"],
        "docs": "/docs",
    }
