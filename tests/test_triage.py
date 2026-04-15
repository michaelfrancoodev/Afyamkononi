"""
Triage Logic Tests — no HTTP, pure unit tests.
Run with: pytest tests/test_triage.py -v
"""

from services.triage import triage, needs_q2
from core.constants import RED, YELLOW, GREEN


# ── Malaria ────────────────────────────────────────────────────
def test_malaria_red():
    assert triage("malaria", "1", "1") == RED

def test_malaria_yellow():
    assert triage("malaria", "1", "2") == YELLOW

def test_malaria_green():
    assert triage("malaria", "2") == GREEN


# ── Pneumonia ──────────────────────────────────────────────────
def test_pneumonia_red():
    assert triage("pneumonia", "1", "1") == RED

def test_pneumonia_yellow():
    assert triage("pneumonia", "1", "2") == YELLOW

def test_pneumonia_green():
    assert triage("pneumonia", "2") == GREEN


# ── Diarrhea ───────────────────────────────────────────────────
def test_diarrhea_red():
    assert triage("diarrhea", "1", "1") == RED

def test_diarrhea_yellow():
    assert triage("diarrhea", "1", "2") == YELLOW

def test_diarrhea_green():
    assert triage("diarrhea", "2") == GREEN


# ── Blood Pressure (1 question only) ──────────────────────────
def test_bp_red():
    assert triage("bp", "1") == RED

def test_bp_yellow():
    assert triage("bp", "2") == YELLOW

def test_bp_no_q2_needed():
    assert needs_q2("bp") is False

def test_others_need_q2():
    for d in ["malaria", "pneumonia", "diarrhea"]:
        assert needs_q2(d) is True


# ── Unknown disease defaults safely ───────────────────────────
def test_unknown_disease_safe():
    result = triage("unknown_disease", "1", "1")
    assert result in (RED, YELLOW, GREEN)
