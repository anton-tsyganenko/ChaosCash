from PyQt6.QtCore import QCoreApplication


def tr(text: str, context: str = "ChaosCash") -> str:
    """Translation wrapper. Uses Qt Linguist."""
    return QCoreApplication.translate(context, text)
