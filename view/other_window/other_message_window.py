from PySide6.QtWidgets import QMessageBox


def show_error(message):
    # Функция для отображения сообщения об ошибке
    error_dialog = QMessageBox()
    error_dialog.setWindowTitle("Ошибка")
    error_dialog.setText(message)
    error_dialog.setIcon(QMessageBox.Warning)
    error_dialog.exec()