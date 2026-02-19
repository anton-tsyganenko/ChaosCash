"""Delegate for date/time fields with timezone handling."""
from PyQt6.QtWidgets import QStyledItemDelegate, QDateTimeEdit
from PyQt6.QtCore import Qt, QDateTime
from datetime import datetime, timezone
import zoneinfo

UTC = timezone.utc


class DateDelegate(QStyledItemDelegate):
    """Displays dates in local time, stores in UTC."""

    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.settings = settings

    def _qt_format(self) -> str:
        return self.settings.date_format  # e.g. "yyyy-MM-dd HH:mm:ss"

    def _local_tz(self):
        try:
            return datetime.now().astimezone().tzinfo
        except Exception:
            return UTC

    def createEditor(self, parent, option, index):
        editor = QDateTimeEdit(parent)
        editor.setCalendarPopup(True)
        editor.setDisplayFormat(self._qt_format())
        return editor

    def setEditorData(self, editor: QDateTimeEdit, index):
        utc_str = index.data(Qt.ItemDataRole.EditRole)
        if utc_str:
            try:
                dt_utc = datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)
                dt_local = dt_utc.astimezone(self._local_tz())
                qt_dt = QDateTime(dt_local.year, dt_local.month, dt_local.day,
                                   dt_local.hour, dt_local.minute, dt_local.second)
                editor.setDateTime(qt_dt)
                return
            except Exception:
                pass
        editor.setDateTime(QDateTime.currentDateTime())

    def setModelData(self, editor: QDateTimeEdit, model, index):
        qt_dt = editor.dateTime()
        local_dt = datetime(qt_dt.date().year(), qt_dt.date().month(), qt_dt.date().day(),
                            qt_dt.time().hour(), qt_dt.time().minute(), qt_dt.time().second(),
                            tzinfo=self._local_tz())
        utc_str = local_dt.astimezone(UTC).strftime("%Y-%m-%d %H:%M:%S")
        model.setData(index, utc_str, Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
