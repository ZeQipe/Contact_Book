from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from view.contacts_list_widget import ContactsListWidget
from view.contact_info_widget import ContactInfoWidget
from tools.handle_manager import *


class MainWindow(QMainWindow):
    def __init__(self, container):
        super().__init__()
        self.container = container
        self.setWindowTitle("Contact Book")
        self.setFixedSize(620, 400)
        self.select_contact = None

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Верхняя часть окна - поиск и создание контакта
        search_layout = QHBoxLayout()
        main_layout.addLayout(search_layout)
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите текст для поиска")
        search_layout.addWidget(self.search_input)

        add_contact_button = QPushButton("Создать контакт")
        add_contact_button.setFixedWidth(self.search_input.sizeHint().width())
        search_layout.addWidget(add_contact_button)

        # Средняя часть окна - список контактов и информация о контакте
        contacts_info_layout = QHBoxLayout()
        main_layout.addLayout(contacts_info_layout)

        self.contacts_list_widget = ContactsListWidget()
        self.contacts_list_widget.setFixedSize(250, 300)
        contacts_info_layout.addWidget(self.contacts_list_widget)

        self.contact_info_widget = ContactInfoWidget()
        self.contact_info_widget.setText("Выберите контакт для просмотра информации")
        contacts_info_layout.addWidget(self.contact_info_widget)

        # Нижняя часть окна - кнопки
        buttons_layout = QHBoxLayout()
        main_layout.addLayout(buttons_layout)

        self.edit_button = QPushButton("Изменить")
        self.edit_button.setStyleSheet("QPushButton { background-color: rgba(255, 255, 255, 100); }")
        self.edit_button.setEnabled(False)  # Делаем кнопку "Изменить" неактивной
        buttons_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Удалить")
        self.delete_button.setStyleSheet("QPushButton { background-color: rgba(255, 255, 255, 100); }")
        self.delete_button.setEnabled(False)  # Делаем кнопку "Удалить" неактивной
        buttons_layout.addWidget(self.delete_button)

        export_button = QPushButton("Экспорт")
        buttons_layout.addWidget(export_button)

        import_button = QPushButton("Импорт")
        buttons_layout.addWidget(import_button)

        #Коннекты для событий
        self.search_input.textChanged.connect(lambda: handle_search(self, self.search_input.text()))
        add_contact_button.clicked.connect(lambda: handle_add_contact(self))
        self.contacts_list_widget.contact_selected.connect(lambda: handle_select_contact(self))
        self.edit_button.clicked.connect(lambda: handle_edit_contact(self))
        self.delete_button.clicked.connect(lambda: handle_delete_button_click(self))
        import_button.clicked.connect(lambda: handle_import_contacts(self))
        export_button.clicked.connect(lambda: handle_export_contacts(self))

        self.update_contacts_list()

    def update_contacts_list(self, contacts: list = None):
        self.contacts_list_widget.clear()

        if contacts:
            for contact in contacts:
                item = QListWidgetItem(str(contact))
                item.setData(Qt.UserRole, contact)
                self.contacts_list_widget.addItem(item)
        else:
            self.contacts_list_widget.clear()
            contacts = self.container.get_contacts()
            for contact in contacts:
                item = QListWidgetItem(str(contact))
                item.setData(Qt.UserRole, contact)
                self.contacts_list_widget.addItem(item)
            self.update_buttons_state(False)

    def update_buttons_state(self, enable):
        self.edit_button.setEnabled(enable)
        self.delete_button.setEnabled(enable)
