import sys
from PySide6.QtWidgets import QApplication
from view.main_window import MainWindow
from core.contact.container import ContainerContact
from tools.loadsaver import load


"""
This class is responsible for the process of launching the main window
"""


class App:
    def __init__(self):
        self.container = self.load_container()

    @staticmethod
    def load_container():
        """
        load container or create new container
        :return: object class ContainerContact
        """
        try:
            return load()
        except Exception as mess:
            print(f'log:application:load_container:18l:{mess}')
            return ContainerContact()

    def run_app(self):
        """
        create main window and show
        :return:
        """
        app = QApplication(sys.argv)
        main_window = MainWindow(self.container)
        main_window.show()
        sys.exit(app.exec())
