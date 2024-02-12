import sys
from PySide6.QtWidgets import QApplication
from view.main_window import MainWindow


class App:

    def __init__(self):
        self.container = self.load_container()

    @staticmethod
    def load_container():
        pass

    def run_app(self):
        app = QApplication(sys.argv)
        main_window = MainWindow(self.container)
        main_window.show()
        sys.exit(app.exec())