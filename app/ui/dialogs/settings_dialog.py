"""Application settings dialog."""
from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
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

        self.decimal_sep = QLineEdit(self.settings.decimal_sep)
        self.decimal_sep.setMaxLength(2)
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

        layout.addWidget(acc_group)

        # Reports group
        reports_group = QGroupBox(tr("Reports"))
        reports_form = QFormLayout(reports_group)

        self.reports_output_dir = QLineEdit(self.settings.reports_output_dir)
        browse_btn = QPushButton(tr("Browse..."))
        browse_btn.clicked.connect(self._browse_reports_output_dir)
        path_layout = QHBoxLayout()
        path_layout.addWidget(self.reports_output_dir)
        path_layout.addWidget(browse_btn)
        reports_form.addRow(tr("Reports output folder:"), path_layout)
        layout.addWidget(reports_group)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._save_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _browse_reports_output_dir(self):
        path = QFileDialog.getExistingDirectory(self, tr("Select Reports Output Folder"), self.reports_output_dir.text())
        if path:
            self.reports_output_dir.setText(path)

    def _save_and_accept(self):
        self.settings.set("date_format", self.date_format.text())
        self.settings.set("decimal_sep", self.decimal_sep.text() or ".")
        sep = self.thousands_sep.text()
        self.settings.set("thousands_sep", sep)
        self.settings.set("account_path_sep", self.path_sep.text() or ":")
        self.settings.set("reports_output_dir", self.reports_output_dir.text())
        self.accept()
