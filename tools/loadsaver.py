import os
import pickle
import csv
from PySide6.QtWidgets import QFileDialog, QMessageBox


def load():
    if os.path.exists(save_path):
        with open(save_path, 'rb') as file:
            return pickle.load(file)
    else:
        raise FileNotFoundError("Файл сохранения не найден.")


def save(data):
    with open(save_path, 'wb') as file:
        pickle.dump(data, file)


def get_and_check_path(save_path: str):
    if not os.path.isdir(save_path + '\\Contacts'):
        os.mkdir(save_path + '\\Contacts')
        return get_and_check_path(save_path)

    if not os.path.isfile(save_path + '\\Contacts\\conbook.jcb'):
        file = open(save_path + '\\Contacts\\conbook.jcb', 'w')
        file.close()
        return get_and_check_path(save_path)

    return save_path + '\\Contacts\\conbook.jcb'


def export_contacts(window):
    # Открываем диалоговое окно для выбора формата сохранения
    file_types = "CSV files (*.csv);;VCF files (*.vcf)"
    format_selected, _ = QFileDialog.getSaveFileName(None, "Выберите формат экспорта", "", file_types)

    if format_selected:
        # Открываем диалоговое окно для выбора места сохранения файла
        file_path, _ = QFileDialog.getSaveFileName(None, "Выберите место сохранения", "", f"{format_selected};;All Files (*)")

        if file_path:
            # Создаем файл и записываем в него информацию о контактах
            try:
                with open(file_path, "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)

                    writer.writerow(["Имя", "Фамилия", "Email", "Номер телефона"])
                    for contact in window.container:
                        writer.writerow([contact.first_name, contact.last_name, contact.email, contact.phone_number])

                QMessageBox.information(None, "Успех", "Контакты успешно экспортированы")
            except Exception as e:
                QMessageBox.critical(None, "Ошибка", f"Не удалось экспортировать контакты: {e}")
        else:
            QMessageBox.critical(None, "Ошибка", "Не выбрано место сохранения")
    else:
        QMessageBox.critical(None, "Ошибка", "Не выбран формат экспорта")


def import_contacts():
    pass


save_path = os.environ.get('LOCALAPPDATA')
save_path = get_and_check_path(save_path)
print(f'log: loadsaver: 41 line (path) - {save_path}')