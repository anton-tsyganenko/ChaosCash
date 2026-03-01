"""Delegate for date/time fields with timezone handling."""
import logging
from datetime import datetime, timezone

from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtWidgets import QDateTimeEdit, QStyledItemDelegate

UTC = timezone.utc


class DateDelegate(QStyledItemDelegate):
    """Displays dates in local time, stores in UTC."""

    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self._logger = logging.getLogger("chaoscash.ui.delegate.date")

    def _qt_format(self) -> str:
        return self.settings.date_format  # e.g. "yyyy-MM-dd HH:mm:ss"

    def _local_tz(self):
        return datetime.now().astimezone().tzinfo

    def createEditor(self, parent, option, index):
        editor = QDateTimeEdit(parent)
        editor.setCalendarPopup(True)
        editor.setDisplayFormat(self._qt_format())
        editor.setKeyboardTracking(False)
        return editor

    def setEditorData(self, editor: QDateTimeEdit, index):
        utc_str = index.data(Qt.ItemDataRole.EditRole)
        if utc_str:
            try:
                dt_utc = datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)
                dt_local = dt_utc.astimezone(self._local_tz())
                qt_dt = QDateTime(
                    dt_local.year, dt_local.month, dt_local.day,
                    dt_local.hour, dt_local.minute, dt_local.second
                )
                editor.setDateTime(qt_dt)
                editor.selectAll()
                return
            except Exception:
                pass
        editor.setDateTime(QDateTime.currentDateTime())
        editor.selectAll()

    def setModelData(self, editor: QDateTimeEdit, model, index):
        qt_dt = editor.dateTime()
        local_dt = datetime(
            qt_dt.date().year(), qt_dt.date().month(), qt_dt.date().day(),
            qt_dt.time().hour(), qt_dt.time().minute(), qt_dt.time().second(),
            tzinfo=self._local_tz()
        )
        utc_str = local_dt.astimezone(UTC).strftime("%Y-%m-%d %H:%M:%S")
        self._logger.debug(
            "setModelData row=%s col=%s qt=%s local=%s utc=%s prev=%r",
            index.row(), index.column(), qt_dt.toString(Qt.DateFormat.ISODate), local_dt.isoformat(), utc_str,
            index.data(Qt.ItemDataRole.EditRole),
        )
        model.setData(index, utc_str, Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
