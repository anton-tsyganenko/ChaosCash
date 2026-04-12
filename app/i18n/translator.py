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
    return _translations.get(text, text)


def load_translations(app: QCoreApplication) -> None:
    """Load translations based on system locale.

    Dynamically loads translations for any language by extracting the language code
    from system locale and merging language JSON files from:
    - translations/<lang>.json (base application strings)
    - app/reports/plugins/**/<lang>.json (report module strings, one file per report folder)

    Falls back to English (source language) for missing keys.

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

    # Load base application translations and optional report module translations
    base_json_file = translations_dir / f"{lang_code}.json"
    report_plugins_dir = Path(__file__).parent.parent / "reports" / "plugins"

    merged: dict[str, str] = {}

    if base_json_file.exists():
        with open(base_json_file, "r", encoding="utf-8") as f:
            merged.update(json.load(f))

    # Scalable structure: one translation file per report folder.
    # Example: app/reports/plugins/account_balances_csv/ru.json
    if report_plugins_dir.exists():
        for report_json_file in sorted(report_plugins_dir.rglob(f"{lang_code}.json")):
            with open(report_json_file, "r", encoding="utf-8") as f:
                merged.update(json.load(f))

    # Fallback: no translation loaded, use English source strings
    _translations = merged
