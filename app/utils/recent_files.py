"""Recent files list stored in QSettings."""
from PyQt6.QtCore import QSettings

MAX_RECENT = 10
_ORG = "chaoscash"
_APP = "chaoscash"
_KEY = "recent_files"


def get_recent_files() -> list[str]:
    settings = QSettings(_ORG, _APP)
    files = settings.value(_KEY, [])
    if isinstance(files, str):
        files = [files] if files else []
    return [f for f in files if f]


def add_recent_file(path: str) -> None:
    files = get_recent_files()
    if path in files:
        files.remove(path)
    files.insert(0, path)
    files = files[:MAX_RECENT]
    settings = QSettings(_ORG, _APP)
    settings.setValue(_KEY, files)


def get_last_file() -> str | None:
    files = get_recent_files()
    return files[0] if files else None
