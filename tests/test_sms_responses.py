"""
AfyaMkononi SMS Response Tests
Test cases with expected outcomes.

Run: python -m pytest tests/test_sms_responses.py -v
"""

import pytest
from services.sms_parser import parse, detect_language
from services.ai_engine import _fallback
from services.health_data import classify_sms_keywords, get_severity

# =============================================================================
# TEST CASES - Questions AI Should Answer Correctly
# =============================================================================

TEST_CASES = [
    # -------------------------------------------------------------------------
    # SWAHILI HEALTH QUESTIONS
    # -------------------------------------------------------------------------
    {
        "input": "nina homa",
        "lang": "sw",
        "expected_contains": ["malaria", "maji", "kupim"],  # Should mention malaria possibility, water, testing
        "should_not_contain": ["samahani", "sijui"],
        "expected_disease": "malaria",
    },
    {
        "input": "kichwa kinauma sana",
        "lang": "sw",
        "expected_contains": ["presha", "pumzika", "maji"],  # BP, rest, water
        "should_not_contain": ["samahani"],
        "expected_disease": "bp",
    },
    {
        "input": "nikilala sana nikija kuamka naona kiza na nahisi kuishiwa nguvu kama nataka kuanguka",
        "lang": "sw",
        "expected_contains": ["presha", "sukari", "lala", "maji"],  # Low BP/sugar, lie down, water
        "should_not_contain": ["samahani", "sijui"],
        "expected_disease": "dizziness",
    },
    {
        "input": "mtoto wangu ana homa na degedege",
        "lang": "sw",
        "expected_contains": ["hospitali", "haraka"],  # Hospital, fast - this is emergency
        "should_not_contain": ["samahani"],
        "expected_severity": "red",
    },
    {
        "input": "nina kuhara maji maji",
        "lang": "sw",
        "expected_contains": ["ors", "maji", "sukari", "chumvi"],  # ORS, water, sugar, salt
        "should_not_contain": ["samahani"],
        "expected_disease": "diarrhea",
    },
    {
        "input": "malaria ilianza lini",
        "lang": "sw",
        "expected_contains": ["afrika", "mbu", "miaka"],  # Africa, mosquito, years
        "should_not_contain": ["samahani", "sijui"],
        "is_history_question": True,
    },
    {
        "input": "typhoid ni nini",
        "lang": "sw",
        "expected_contains": ["tumbo", "maji", "chakula"],  # Stomach, water, food
        "should_not_contain": ["samahani", "sijui"],
        "is_history_question": True,
    },
    
    # -------------------------------------------------------------------------
    # ENGLISH HEALTH QUESTIONS
    # -------------------------------------------------------------------------
    {
        "input": "I have fever and chills",
        "lang": "en",
        "expected_contains": ["malaria", "water", "test"],
        "should_not_contain": ["sorry", "apologize"],
        "expected_disease": "malaria",
    },
    {
        "input": "my head hurts so bad",
        "lang": "en",
        "expected_contains": ["bp", "rest", "water"],
        "should_not_contain": ["sorry"],
        "expected_disease": "bp",
    },
    {
        "input": "when I stand up I feel dizzy and see darkness",
        "lang": "en",
        "expected_contains": ["pressure", "sugar", "lie down"],
        "should_not_contain": ["sorry", "don't know"],
        "expected_disease": "dizziness",
    },
    {
        "input": "my child has high fever and seizures",
        "lang": "en",
        "expected_contains": ["hospital", "emergency", "fast"],
        "should_not_contain": ["sorry"],
        "expected_severity": "red",
    },
    {
        "input": "when did malaria start",
        "lang": "en",
        "expected_contains": ["africa", "mosquito", "years", "thousand"],
        "should_not_contain": ["sorry", "don't know"],
        "is_history_question": True,
    },
    
    # -------------------------------------------------------------------------
    # GREETINGS - Should respond warmly, not apologize
    # -------------------------------------------------------------------------
    {
        "input": "habari",
        "lang": "sw",
        "expected_contains": ["habari", "afyamkononi", "saidia"],
        "should_not_contain": ["samahani"],
        "is_greeting": True,
    },
    {
        "input": "hi",
        "lang": "en",
        "expected_contains": ["hi", "afyamkononi", "help"],
        "should_not_contain": ["sorry"],
        "is_greeting": True,
    },
    {
        "input": "mambo vipi",
        "lang": "sw",
        "expected_contains": ["afyamkononi"],
        "should_not_contain": ["samahani"],
        "is_greeting": True,
    },
    
    # -------------------------------------------------------------------------
    # EMERGENCY - Should be RED severity
    # -------------------------------------------------------------------------
    {
        "input": "mtu wangu amepoteza fahamu",
        "lang": "sw",
        "expected_contains": ["hospitali", "dharura", "sasa"],
        "expected_severity": "red",
        "is_emergency": True,
    },
    {
        "input": "my wife is unconscious and not breathing",
        "lang": "en",
        "expected_contains": ["hospital", "emergency", "now"],
        "expected_severity": "red",
        "is_emergency": True,
    },
    {
        "input": "ana degedege sasa hivi",
        "lang": "sw",
        "expected_contains": ["hospitali", "haraka"],
        "expected_severity": "red",
        "is_emergency": True,
    },
]


class TestLanguageDetection:
    """Test language detection accuracy."""
    
    def test_swahili_detection(self):
        assert detect_language("nina homa") == "sw"
        assert detect_language("kichwa kinauma") == "sw"
        assert detect_language("mtoto wangu ana kuhara") == "sw"
        assert detect_language("habari yako") == "sw"
    
    def test_english_detection(self):
        assert detect_language("I have fever") == "en"
        assert detect_language("my head hurts") == "en"
        assert detect_language("my child has diarrhea") == "en"
        assert detect_language("hello how are you") == "en"


class TestDiseaseClassification:
    """Test disease keyword classification."""
    
    def test_malaria_keywords(self):
        assert classify_sms_keywords("nina homa na baridi") == "malaria"
        assert classify_sms_keywords("i have fever and chills") == "malaria"
    
    def test_diarrhea_keywords(self):
        assert classify_sms_keywords("nina kuhara maji") == "diarrhea"
        assert classify_sms_keywords("i have diarrhea") == "diarrhea"
    
    def test_bp_keywords(self):
        assert classify_sms_keywords("nina kizunguzungu") in ["bp", "dizziness"]
        assert classify_sms_keywords("i feel dizzy") in ["bp", "dizziness"]
    
    def test_pneumonia_keywords(self):
        assert classify_sms_keywords("nina kikohozi na pumzi shida") == "pneumonia"


class TestSeverityDetection:
    """Test severity level detection."""
    
    def test_red_severity(self):
        assert get_severity("malaria", "ana degedege") == "red"
        assert get_severity("bp", "ganzi upande mmoja") == "red"
        assert get_severity("diarrhea", "macho yamezama") == "red"
    
    def test_yellow_severity(self):
        assert get_severity("malaria", "ana homa") == "yellow"
        assert get_severity("bp", "kichwa kinauma") == "yellow"


class TestFallbackResponses:
    """Test fallback responses are accurate and don't apologize."""
    
    def test_swahili_fallback_no_apology(self):
        for keyword in ["homa", "kichwa", "kuhara", "kizunguzungu"]:
            response = _fallback(keyword, "sw")
            assert "samahani" not in response.lower()
            assert len(response) < 350  # SMS length
    
    def test_english_fallback_no_apology(self):
        for keyword in ["fever", "headache", "diarrhea", "dizzy"]:
            response = _fallback(keyword, "en")
            assert "sorry" not in response.lower()
            assert len(response) < 350
    
    def test_dizziness_fallback(self):
        response = _fallback("nahisi kizunguzungu na kuona kiza", "sw")
        assert "presha" in response.lower() or "sukari" in response.lower()
        assert "samahani" not in response.lower()
    
    def test_malaria_history_fallback(self):
        response = _fallback("malaria ilianza lini", "sw")
        assert "afrika" in response.lower() or "mbu" in response.lower()


class TestSMSParser:
    """Test SMS parsing functionality."""
    
    def test_greeting_detection(self):
        result = parse("habari")
        assert result["is_greeting"] == True
        assert "samahani" not in result["response"].lower()
        
        result = parse("hi")
        assert result["is_greeting"] == True
        assert "sorry" not in result["response"].lower()
    
    def test_emergency_detection(self):
        result = parse("mtu wangu amepoteza fahamu")
        assert result["is_emergency"] == True
        assert "hospitali" in result["response"].lower() or "dharura" in result["response"].lower()
        
        result = parse("my friend is unconscious")
        assert result["is_emergency"] == True
    
    def test_health_question_uses_ai(self):
        result = parse("nina homa na maumivu ya kichwa")
        assert result["use_ai"] == True
        assert result["disease"] == "malaria"


# =============================================================================
# EXPECTED OUTCOMES REFERENCE
# =============================================================================

EXPECTED_OUTCOMES = """
==============================================================================
MASWALI NA MAJIBU YANAYOTAKIWA (Test Reference)
==============================================================================

1. SWALI: "nina homa"
   JIBU LINATARAJIWA: "Homa inaweza kuwa malaria au mafua. Kunywa maji mengi, pumzika. Fika kupima damu - usitumie dawa bila kupimwa."
   SEVERITY: yellow

2. SWALI: "nikilala sana nikija kuamka naona kiza na nahisi kuishiwa nguvu"
   JIBU LINATARAJIWA: "Dalili hizi zinaweza kuwa presha chini au sukari chini. Lala chini sasa, kunywa maji na sukari kidogo. Fika kituo cha afya kupima presha na damu."
   SEVERITY: yellow

3. SWALI: "malaria ilianza lini"
   JIBU LINATARAJIWA: "Malaria imekuwepo Afrika kwa maelfu ya miaka, inaenezwa na mbu aina ya Anopheles. Una swali la kiafya?"
   SEVERITY: green

4. SWALI: "habari"
   JIBU LINATARAJIWA: "Habari! Mimi ni AfyaMkononi. Nikuasaidie nini leo? Niambie unavyojisikia."
   SEVERITY: green

5. SWALI: "mtoto wangu ana degedege"
   JIBU LINATARAJIWA: "Hii ni DHARURA! Dalili hizi ni hatari sana. Fika HOSPITALI SASA..."
   SEVERITY: red

6. SWALI: "I have fever and body aches"
   EXPECTED: "Fever could be malaria or flu. Drink lots of water, rest. Get a blood test - don't take medicine without testing."
   SEVERITY: yellow

7. SWALI: "when did malaria start"
   EXPECTED: "Malaria has existed in Africa for thousands of years, spread by Anopheles mosquitoes. Any health question?"
   SEVERITY: green

==============================================================================
MAMBO YA KUANGALIA:
- Hakuna "samahani" au "sorry" katika majibu
- Majibu ni mafupi (sentensi 2-3)
- Kila jibu la afya linaishia na pendekezo la kituo cha afya
- Dalili za hatari zinapata severity=red
- Kiswahili ni rahisi na cha kawaida
==============================================================================
"""

if __name__ == "__main__":
    print(EXPECTED_OUTCOMES)
    pytest.main([__file__, "-v"])
