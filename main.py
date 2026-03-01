"""ChaosCash — Personal accounting application. Entry point."""
import argparse
import logging
import os
import sys

# Ensure the project root is in the path
sys.path.insert(0, os.path.dirname(__file__))

from PyQt6.QtWidgets import QApplication

from app.settings.app_settings import AppSettings
from app.ui.main_window import MainWindow
from app.ui.ui_event_logger import UIEventLogger
from app.utils.recent_files import get_last_file


def _configure_logging(enabled: bool) -> None:
    """Configure logging only when explicitly enabled via CLI."""
    root = logging.getLogger()
    root.handlers.clear()

    if not enabled:
        root.setLevel(logging.WARNING)
        return

    root.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)
    logging.getLogger(__name__).info("Debug logging enabled (terminal only)")


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ChaosCash")
    parser.add_argument("db_path", nargs="?", help="Path to .ccash/.db file")
    parser.add_argument(
        "--debug-logging",
        action="store_true",
        help="Enable verbose debug logging to terminal",
    )
    return parser.parse_args(argv)


def main():
    args = _parse_args(sys.argv[1:])
    _configure_logging(args.debug_logging)

    app = QApplication(sys.argv)
    app.setOrganizationName("chaoscash")
    app.setApplicationName("chaoscash")
    app.setApplicationDisplayName("ChaosCash")

    settings = AppSettings()

    if args.debug_logging:
        ui_event_logger = UIEventLogger(app)
        ui_event_logger.install(app)
        app.setProperty("ui_event_logger", ui_event_logger)

    # Determine which file to open
    db_path = args.db_path or get_last_file()

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
    from PyQt6.QtWidgets import (
        QDialog,
        QFileDialog,
        QHBoxLayout,
        QLabel,
        QPushButton,
        QVBoxLayout,
    )

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
