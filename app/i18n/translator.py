import os
from pathlib import Path

from PyQt6.QtCore import QCoreApplication, QLocale, QTranslator


def tr(text: str, context: str = "ChaosCash") -> str:
    """Translation wrapper. Uses Qt Linguist."""
    return QCoreApplication.translate(context, text)


def load_translations(app: QCoreApplication) -> None:
    """Load translations based on system locale.

    Loads Russian translation if system locale is ru_*.
    Falls back to English (source language) otherwise.

    Args:
        app: QApplication instance to install translator into
    """
    # Get translations directory
    translations_dir = Path(__file__).parent.parent.parent / "translations"

    # Detect system locale
    system_locale = QLocale.system()

    # Try to load Russian translation if locale matches
    if system_locale.language() == QLocale.Language.Russian:
        qm_file = translations_dir / "chaoscash_ru.qm"

        # Only load if file exists
        if qm_file.exists():
            translator = QTranslator()
            if translator.load(str(qm_file)):
                app.installTranslator(translator)
                return

    # Fallback: no translation loaded, use English source strings
