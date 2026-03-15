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

    Loads Russian translation from JSON if system locale is ru_*.
    Falls back to English (source language) otherwise.

    Args:
        app: QApplication instance (used for compatibility, not strictly needed for JSON)
    """
    global _translations

    # Get translations directory
    translations_dir = Path(__file__).parent.parent.parent / "translations"

    # Detect system locale
    system_locale = QLocale.system()

    # Try to load Russian translation if locale matches
    if system_locale.language() == QLocale.Language.Russian:
        json_file = translations_dir / "ru.json"

        # Only load if file exists
        if json_file.exists():
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    _translations = json.load(f)
                return
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to load translations from {json_file}: {e}")

    # Fallback: no translation loaded, use English source strings
    _translations = {}
