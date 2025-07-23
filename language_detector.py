from langdetect import detect, DetectorFactory

# Makes language detection more consistent
DetectorFactory.seed = 0

def detect_language(text):
    """
    Detects the ISO language code (e.g., 'en', 'hi', 'bn') from a given text input.
    Returns abbreviation (ISO 639-1 Code) — full names mapped in app.py.
    """
    # ✅ Safety check: at least a few characters
    if not text or len(text.strip()) < 3:
        return "unknown"

    try:
        lang_code = detect(text)
        return lang_code
    except Exception:
        return "unknown"
