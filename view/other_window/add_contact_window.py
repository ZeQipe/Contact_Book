from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator


class AddDialogWindow(QDialog):
    save_clicked = Signal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Создать контакт")

        # Создаем метки и поля ввода для данных контакта
        self.first_name_label = QLabel("*Имя:")
        self.first_name_input = QLineEdit()
        self.last_name_label = QLabel("Фамилия:")
        self.last_name_input = QLineEdit()
        self.phone_label = QLabel("*Номер:")
        self.phone_input = QLineEdit()
        validator = QRegularExpressionValidator(QRegularExpression("[0-9+]*"), self.phone_input)
        self.phone_input.setValidator(validator)
        self.email_label = QLabel("Почтовый адрес:")
        self.email_input = QLineEdit()

        # Кнопки "Сохранить" и "Отменить"
        self.save_button = QPushButton("Сохранить")
        self.cancel_button = QPushButton("Отменить")

        # Создаем макет для размещения виджетов в диалоговом окне
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Добавляем метки и поля ввода в макет
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Создаем горизонтальный макет для кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)

        # Добавляем макет с кнопками в основной макет
        layout.addLayout(button_layout)
        self.save_button.clicked.connect(self.emit_save_signal)
        self.cancel_button.clicked.connect(lambda: self.reject())

    def emit_save_signal(self):
        # Отправляем сигнал с данными при сохранении
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        self.save_clicked.emit(first_name, last_name, phone, email)
