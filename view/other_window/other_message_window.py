from PySide6.QtWidgets import QMessageBox


def show_error(message):
    # Функция для отображения сообщения об ошибке
    error_dialog = QMessageBox()
    error_dialog.setWindowTitle("Ошибка")
    error_dialog.setText(message)
    error_dialog.setIcon(QMessageBox.Warning)
    error_dialog.exec()


def approv_delete_window(target):
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Подтверждение удаления")
    msg_box.setText(
        f"Вы действительно хотите удалить контакт: {target.get_first_name()} {target.get_last_name()}?")
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Cancel)
    msg_box.setIcon(QMessageBox.Question)
    return msg_box.exec()