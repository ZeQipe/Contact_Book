import sys
from PySide6.QtWidgets import QApplication
from view.main_window import MainWindow
from core.contact.container import ContainerContact
from tools.loadsaver import load


class App:

    def __init__(self):
        self.container = self.load_container()

    @staticmethod
    def load_container():
        try:
            return load()
        except Exception as mess:
            print(f'log: application: 18 line - {mess}')
            return ContainerContact()

    def run_app(self):
        app = QApplication(sys.argv)
        main_window = MainWindow(self.container)
        main_window.show()
        sys.exit(app.exec())