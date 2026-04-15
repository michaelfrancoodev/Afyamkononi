"""
USSD Flow Tests.

Simulates Africa's Talking POST requests directly to our handler.
Run with: pytest tests/test_ussd.py -v
"""

import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.fixture
def client():
    return AsyncClient(transport=ASGITransport(app=app), base_url="http://test")


def ussd_payload(session_id: str, phone: str, text: str) -> dict:
    return {
        "sessionId":   session_id,
        "phoneNumber": phone,
        "text":        text,
        "serviceCode": "*2392#",
    }


# ── Welcome screen ────────────────────────────────────────────
@pytest.mark.asyncio
async def test_welcome_screen(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s1", "+255700000001", ""))
    assert r.status_code == 200
    assert r.text.startswith("CON")
    assert "Kiswahili" in r.text


# ── Language selection ─────────────────────────────────────────
@pytest.mark.asyncio
async def test_select_swahili(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s2", "+255700000002", "1"))
    assert "CON" in r.text
    assert "tatizo" in r.text.lower()   # Swahili main menu


@pytest.mark.asyncio
async def test_select_english(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s3", "+255700000003", "2"))
    assert "CON" in r.text
    assert "issue" in r.text.lower()    # English main menu


# ── Malaria flow — RED path ────────────────────────────────────
@pytest.mark.asyncio
async def test_malaria_red(client):
    """1 (sw) → 1 (malaria) → 1 (fever yes) → 1 (confusion yes) = RED"""
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s4", "+255700000004", "1*1*1*1"))
    assert r.text.startswith("END")
    assert "DHARURA" in r.text.upper()


# ── Malaria flow — YELLOW path ─────────────────────────────────
@pytest.mark.asyncio
async def test_malaria_yellow(client):
    """1 (sw) → 1 (malaria) → 1 (fever yes) → 2 (no confusion) = YELLOW"""
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s5", "+255700000005", "1*1*1*2"))
    assert r.text.startswith("END")
    assert "MALARIA" in r.text.upper()
    assert "DHARURA" not in r.text.upper()


# ── Malaria flow — GREEN path ──────────────────────────────────
@pytest.mark.asyncio
async def test_malaria_green(client):
    """1 (sw) → 1 (malaria) → 2 (no fever) = GREEN"""
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s6", "+255700000006", "1*1*2"))
    assert r.text.startswith("END")
    assert "DHARURA" not in r.text.upper()


# ── BP flow — RED path (1 question only) ──────────────────────
@pytest.mark.asyncio
async def test_bp_red(client):
    """1 (sw) → 4 (bp) → 1 (stroke signs yes) = RED immediately"""
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s7", "+255700000007", "1*4*1"))
    assert r.text.startswith("END")
    assert "DHARURA" in r.text.upper()


# ── BP flow — YELLOW ──────────────────────────────────────────
@pytest.mark.asyncio
async def test_bp_yellow(client):
    """1 (sw) → 4 (bp) → 2 (no stroke) = YELLOW"""
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s8", "+255700000008", "1*4*2"))
    assert r.text.startswith("END")
    assert "BP" in r.text.upper() or "SHINIKIZO" in r.text.upper()


# ── Other symptoms ─────────────────────────────────────────────
@pytest.mark.asyncio
async def test_other_symptoms(client):
    """1 (sw) → 5 (other) = safety net"""
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s9", "+255700000009", "1*5"))
    assert r.text.startswith("END")
    assert "kituo" in r.text.lower()


# ── Exit ───────────────────────────────────────────────────────
@pytest.mark.asyncio
async def test_exit_from_main(client):
    """1 (sw) → 0 (exit) = goodbye"""
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s10", "+255700000010", "1*0"))
    assert r.text.startswith("END")
    assert "2392" in r.text


# ── Health ping ────────────────────────────────────────────────
@pytest.mark.asyncio
async def test_ping(client):
    async with client as c:
        r = await c.get("/ping")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
