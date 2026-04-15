from core.constants import LANG_SW, SCREENS, RESULTS


def screen(name: str, lang: str) -> tuple[str, str]:
    key = f"{name}_{lang}"
    if key in SCREENS:
        return SCREENS[key]
    if key in RESULTS:
        return RESULTS[key]
    # fall back to Swahili if English version not found
    sw_key = f"{name}_{LANG_SW}"
    if sw_key in SCREENS:
        return SCREENS[sw_key]
    if sw_key in RESULTS:
        return RESULTS[sw_key]
    raise KeyError(f"Screen not found: {key}")


def result(severity: str, disease: str, lang: str) -> tuple[str, str]:
    if severity == "green":
        key = f"green_{lang}"
    elif severity == "other" or disease == "other":
        key = f"other_{lang}"
    else:
        key = f"{severity}_{disease}_{lang}"

    if key in RESULTS:
        return RESULTS[key]
    # fallback chain
    fallback = RESULTS.get(
        f"{severity}_{disease}_{LANG_SW}",
        RESULTS.get(f"other_{LANG_SW}")
    )
    return fallback


def exit_screen(lang: str) -> tuple[str, str]:
    return RESULTS.get(f"exit_{lang}", RESULTS["exit_sw"])
