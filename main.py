"""ChaosCash — Personal accounting application. Entry point."""
import sys
import os
import logging

# Ensure the project root is in the path
sys.path.insert(0, os.path.dirname(__file__))

from PyQt6.QtWidgets import QApplication, QFileDialog
from PyQt6.QtCore import QCoreApplication, QSettings

from app.settings.app_settings import AppSettings
from app.utils.recent_files import get_last_file
from app.ui.main_window import MainWindow
from app.ui.ui_event_logger import UIEventLogger


def _configure_logging() -> None:
    """Configure verbose logging for UI focus/edit diagnostics."""
    log_path = os.path.join(os.getcwd(), "chaoscash_ui_debug.log")
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    if not root.handlers:
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        root.addHandler(console_handler)

    logging.getLogger(__name__).info("Logging enabled, output file: %s", log_path)


def main():
    _configure_logging()
    app = QApplication(sys.argv)
    app.setOrganizationName("chaoscash")
    app.setApplicationName("chaoscash")
    app.setApplicationDisplayName("ChaosCash")

    settings = AppSettings()

    ui_event_logger = UIEventLogger(app)
    ui_event_logger.install(app)
    app.setProperty("ui_event_logger", ui_event_logger)

    # Determine which file to open
    db_path = None
    if len(sys.argv) > 1:
        db_path = sys.argv[1]
    else:
        db_path = get_last_file()

    if db_path and not os.path.exists(db_path):
        db_path = None

    if db_path is None:
        # Ask user to open or create a file
        choice = _ask_file_path()
        if choice is None:
            return
        db_path = choice

    window = MainWindow(db_path, settings)
    window.show()

    sys.exit(app.exec())


def _ask_file_path() -> str | None:
    """Show file picker to open or create a database."""
    from PyQt6.QtWidgets import QFileDialog, QMessageBox, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QLabel

    class StartupDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ChaosCash")
            self.path = None
            layout = QVBoxLayout(self)
            layout.addWidget(QLabel("Welcome to ChaosCash\n\nOpen an existing database or create a new one."))
            btn_layout = QHBoxLayout()
            btn_open = QPushButton("Open existing...")
            btn_new = QPushButton("Create new...")
            btn_cancel = QPushButton("Cancel")
            btn_open.clicked.connect(self._open)
            btn_new.clicked.connect(self._new)
            btn_cancel.clicked.connect(self.reject)
            btn_layout.addWidget(btn_open)
            btn_layout.addWidget(btn_new)
            btn_layout.addWidget(btn_cancel)
            layout.addLayout(btn_layout)

        def _open(self):
            path, _ = QFileDialog.getOpenFileName(
                self, "Open Database", "",
                "ChaosCash Database (*.ccash *.db);;All Files (*)"
            )
            if path:
                self.path = path
                self.accept()

        def _new(self):
            path, _ = QFileDialog.getSaveFileName(
                self, "New Database", "",
                "ChaosCash Database (*.ccash *.db);;All Files (*)"
            )
            if path:
                self.path = path
                self.accept()

    dlg = StartupDialog()
    if dlg.exec():
        return dlg.path
    return None


if __name__ == "__main__":
    main()
