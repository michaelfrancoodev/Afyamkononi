from core.constants import RED, YELLOW, GREEN


def triage(disease: str, q1: str, q2: str | None = None) -> str:
    """
    Returns RED, YELLOW, or GREEN based on the disease and answers.

    q1 and q2 are "1" for yes, "2" for no.
    BP only uses q1 since the first question already covers stroke signs.
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
        if q1 == yes:
            return RED
        return YELLOW

    # unknown disease - default to yellow so user still gets clinic advice
    return YELLOW


def needs_q2(disease: str) -> bool:
    return disease != "bp"
