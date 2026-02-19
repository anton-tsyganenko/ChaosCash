"""Application settings dialog."""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QComboBox,
    QDialogButtonBox, QGroupBox
)
from app.i18n import tr
from app.settings.app_settings import AppSettings


class SettingsDialog(QDialog):
    def __init__(self, settings: AppSettings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.setWindowTitle(tr("Settings"))
        self.setModal(True)
        self.setMinimumWidth(400)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        # Display group
        display_group = QGroupBox(tr("Display"))
        form = QFormLayout(display_group)

        self.date_format = QLineEdit(self.settings.date_format)
        form.addRow(tr("Date format:"), self.date_format)

        self.decimal_sep = QComboBox()
        self.decimal_sep.addItems([".", ","])
        self.decimal_sep.setCurrentText(self.settings.decimal_sep)
        form.addRow(tr("Decimal separator:"), self.decimal_sep)

        self.thousands_sep = QLineEdit(self.settings.thousands_sep)
        self.thousands_sep.setPlaceholderText(tr("Leave empty to disable"))
        self.thousands_sep.setMaxLength(4)
        form.addRow(tr("Thousands separator:"), self.thousands_sep)

        layout.addWidget(display_group)

        # Accounts group
        acc_group = QGroupBox(tr("Accounts"))
        acc_form = QFormLayout(acc_group)

        self.path_sep = QLineEdit(self.settings.account_path_sep)
        acc_form.addRow(tr("Account path separator:"), self.path_sep)

        self.sort_order = QComboBox()
        self.sort_order.addItem(tr("By name"), "name")
        self.sort_order.addItem(tr("By code"), "code")
        self.sort_order.addItem(tr("Name then code"), "name_code")
        self.sort_order.addItem(tr("Code then name"), "code_name")
        idx = self.sort_order.findData(self.settings.account_sort)
        if idx >= 0:
            self.sort_order.setCurrentIndex(idx)
        acc_form.addRow(tr("Sort accounts:"), self.sort_order)
        layout.addWidget(acc_group)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._save_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _save_and_accept(self):
        self.settings.set("date_format", self.date_format.text())
        self.settings.set("decimal_sep", self.decimal_sep.currentText())
        sep = self.thousands_sep.text()
        self.settings.set("thousands_sep", sep)
        self.settings.set("show_thousands", bool(sep))
        self.settings.set("account_path_sep", self.path_sep.text() or ":")
        self.settings.set("account_sort", self.sort_order.currentData())
        self.accept()
