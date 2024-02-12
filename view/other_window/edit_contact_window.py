from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator


class EditDialogWindow(QDialog):
    save_clicked = Signal()

    def __init__(self, contact):
        super().__init__()
        self.contact = contact
        self.setWindowTitle("Редактировать контакт")

        layout = QVBoxLayout()

        # Поля для редактирования информации о контакте
        self.first_name_input = QLineEdit(self.contact.get_first_name())
        layout.addWidget(QLabel("Имя:"))
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit(self.contact.get_last_name())
        layout.addWidget(QLabel("Фамилия:"))
        layout.addWidget(self.last_name_input)

        self.phone_input = QLineEdit(self.contact.get_phone_number())
        layout.addWidget(QLabel("Телефон:"))
        validator = QRegularExpressionValidator(QRegularExpression("[0-9+]*"), self.phone_input)
        self.phone_input.setValidator(validator)
        layout.addWidget(self.phone_input)

        self.email_input = QLineEdit(self.contact.get_email())
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        # Кнопки для сохранения и отмены
        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.handle_save)
        layout.addWidget(save_button)

        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.reject)
        layout.addWidget(cancel_button)

        self.setLayout(layout)

    def handle_save(self):
        self.save_clicked.emit()
        self.accept()

    def get_contact_data(self):
        # Получение новых данных контакта из полей ввода
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        return [first_name, last_name, phone, email]
