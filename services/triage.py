from core.constants import RED, YELLOW, GREEN


def triage(disease: str, q1: str, q2: str | None = None) -> str:
    """
    Returns RED, YELLOW, or GREEN based on disease and answers.
    q1 and q2 are "1" for yes, "2" for no.

    Malaria:   q1=yes + q2=yes -> RED,    q1=yes -> YELLOW,  q1=no -> GREEN
    Pneumonia: q1=yes + q2=yes -> RED,    q1=yes -> YELLOW,  q1=no -> GREEN
    Diarrhea:  q1=yes + q2=yes -> RED,    q1=yes -> YELLOW,  q1=no -> GREEN
    BP:        q1=yes          -> RED,    q1=no  -> q2=yes -> YELLOW, q2=no -> GREEN
    """
    yes = "1"

    if disease == "malaria":
        if q1 == yes and q2 == yes:
            return RED
        if q1 == yes:
            return YELLOW
        return GREEN

    if disease == "pneumonia":
        if q1 == yes and q2 == yes:
            return RED
        if q1 == yes:
            return YELLOW
        return GREEN

    if disease == "diarrhea":
        if q1 == yes and q2 == yes:
            return RED
        if q1 == yes:
            return YELLOW
        return GREEN

    if disease == "bp":
        # Q1 asks stroke signs - if yes, emergency immediately
        if q1 == yes:
            return RED
        # Q1 no, Q2 asks severe headache/dizziness
        if q2 == yes:
            return YELLOW
        return GREEN

    return YELLOW


def needs_q2(disease: str) -> bool:
    # All diseases now have 2 questions
    return True
