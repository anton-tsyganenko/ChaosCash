import json
from pathlib import Path

from PyQt6.QtCore import QCoreApplication, QLocale


# Module-level dictionary to store loaded translations
_translations = {}


def tr(text: str, context: str = "ChaosCash") -> str:
    """Translation wrapper. Returns translated string or falls back to English.

    Args:
        text: English text to translate
        context: Translation context (for compatibility with Qt)

    Returns:
        Translated string if available, otherwise the English source text
    """
    # Check if translation exists in loaded translations
    if text in _translations:
        return _translations[text]

    # Fallback to English source text
    return text


def load_translations(app: QCoreApplication) -> None:
    """Load translations based on system locale.

    Dynamically loads translations for any language by extracting the language code
    from system locale and loading the corresponding JSON file from translations/.
    Falls back to English (source language) if translation file doesn't exist.

    Supports any language: ru.json, fr.json, de.json, etc.

    Args:
        app: QApplication instance (used for compatibility, not strictly needed for JSON)
    """
    global _translations

    # Get translations directory
    translations_dir = Path(__file__).parent.parent.parent / "translations"

    # Detect system locale and extract language code
    system_locale = QLocale.system()

    # Get language code from locale (e.g., "ru" from ru_RU, "en" from en_US)
    # Use bcp47Name() which returns format like "ru" or "en-US"
    locale_name = system_locale.bcp47Name()
    lang_code = locale_name.split('-')[0].lower()  # Get part before dash

    # Try to load translation file for detected language
    json_file = translations_dir / f"{lang_code}.json"

    if json_file.exists():
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                _translations = json.load(f)
            print(f"Loaded translations from {json_file.name}")
            return
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load translations from {json_file}: {e}")

    # Fallback: no translation loaded, use English source strings
    print(f"No translation file found for language '{lang_code}' (looked for {json_file.name})")
    _translations = {}
