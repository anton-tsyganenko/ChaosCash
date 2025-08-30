import sys
from PyQt6.QtWidgets import QApplication
from db import Database
from main_controller import MainController

if __name__ == '__main__':
    db = Database('finance.db')
    app = QApplication(sys.argv)
    controller = MainController(db)
    controller.show_view()
    sys.exit(app.exec())
