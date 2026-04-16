from services.triage import triage, needs_q2
from core.constants import RED, YELLOW, GREEN


def test_malaria_red():
    assert triage("malaria", "1", "1") == RED


def test_malaria_yellow():
    assert triage("malaria", "1", "2") == YELLOW


def test_malaria_green():
    assert triage("malaria", "2", "2") == GREEN


def test_pneumonia_red():
    assert triage("pneumonia", "1", "1") == RED


def test_pneumonia_yellow():
    assert triage("pneumonia", "1", "2") == YELLOW


def test_pneumonia_green():
    assert triage("pneumonia", "2", "2") == GREEN


def test_diarrhea_red():
    assert triage("diarrhea", "1", "1") == RED


def test_diarrhea_yellow():
    assert triage("diarrhea", "1", "2") == YELLOW


def test_diarrhea_green():
    assert triage("diarrhea", "2", "2") == GREEN


def test_bp_red():
    # Stroke signs = RED immediately
    assert triage("bp", "1") == RED


def test_bp_yellow():
    # No stroke, but severe headache/dizziness
    assert triage("bp", "2", "1") == YELLOW


def test_bp_green():
    # No stroke, no severe symptoms
    assert triage("bp", "2", "2") == GREEN


def test_all_need_q2():
    for d in ["malaria", "pneumonia", "diarrhea", "bp"]:
        assert needs_q2(d) is True


def test_unknown_disease_safe():
    assert triage("unknown", "1", "1") in (RED, YELLOW, GREEN)
