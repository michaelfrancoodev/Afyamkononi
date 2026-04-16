import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.fixture
def client():
    return AsyncClient(transport=ASGITransport(app=app), base_url="http://test")


def ussd_payload(session_id, phone, text):
    return {
        "sessionId":   session_id,
        "phoneNumber": phone,
        "text":        text,
        "serviceCode": "*24929#",
    }


@pytest.mark.asyncio
async def test_welcome_screen(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s1", "+255700000001", ""))
    assert r.status_code == 200
    assert r.text.startswith("CON")
    assert "Kiswahili" in r.text


@pytest.mark.asyncio
async def test_select_swahili(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s2", "+255700000002", "1"))
    assert "CON" in r.text
    assert "tatizo" in r.text.lower()


@pytest.mark.asyncio
async def test_select_english(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s3", "+255700000003", "2"))
    assert "CON" in r.text
    assert "problem" in r.text.lower()


@pytest.mark.asyncio
async def test_malaria_red(client):
    # sw -> malaria -> q1=yes -> q2=yes = RED
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s4", "+255700000004", "1*1*1*1"))
    assert r.text.startswith("END")
    assert "DHARURA" in r.text.upper()


@pytest.mark.asyncio
async def test_malaria_yellow(client):
    # sw -> malaria -> q1=yes -> q2=no = YELLOW
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s5", "+255700000005", "1*1*1*2"))
    assert r.text.startswith("END")
    assert "MALARIA" in r.text.upper()
    assert "DHARURA" not in r.text.upper()


@pytest.mark.asyncio
async def test_malaria_green(client):
    # sw -> malaria -> q1=no -> q2=no = GREEN
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s6", "+255700000006", "1*1*2*2"))
    assert r.text.startswith("END")
    assert "MAPUMZIKO" in r.text.upper() or "REST" in r.text.upper()


@pytest.mark.asyncio
async def test_bp_red(client):
    # sw -> bp -> q1=yes (stroke signs) = RED immediately
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s7", "+255700000007", "1*4*1"))
    assert r.text.startswith("END")
    assert "DHARURA" in r.text.upper()


@pytest.mark.asyncio
async def test_bp_yellow(client):
    # sw -> bp -> q1=no -> q2=yes (severe headache) = YELLOW
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s8", "+255700000008", "1*4*2*1"))
    assert r.text.startswith("END")
    assert "DHARURA" not in r.text.upper()


@pytest.mark.asyncio
async def test_bp_green(client):
    # sw -> bp -> q1=no -> q2=no = GREEN
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s9", "+255700000009", "1*4*2*2"))
    assert r.text.startswith("END")
    assert "MAPUMZIKO" in r.text.upper() or "REST" in r.text.upper()


@pytest.mark.asyncio
async def test_other_symptoms(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s10", "+255700000010", "1*5"))
    assert r.text.startswith("END")
    assert "zahanati" in r.text.lower() or "daktari" in r.text.lower() or "health" in r.text.lower()


@pytest.mark.asyncio
async def test_exit(client):
    async with client as c:
        r = await c.post("/ussd", data=ussd_payload("s11", "+255700000011", "1*0"))
    assert r.text.startswith("END")
    assert "24929" in r.text


@pytest.mark.asyncio
async def test_ping(client):
    async with client as c:
        r = await c.get("/ping")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
