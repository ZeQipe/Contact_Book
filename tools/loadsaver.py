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


def export_contacts(contacts):
    file_path, _ = QFileDialog.getSaveFileName(None, "Выберите место сохранения", "",
                                               "CSV Files (*.csv);;VCF Files (*.vcf)")

    if file_path:
        try:
            format_selected = "CSV" if file_path.endswith(".csv") else "VCF"

            if format_selected == "CSV":
                with open(file_path, "w", encoding="utf-8-sig") as file:
                    file.write('Name;SurName;Number Phone; EMail Address;\n')
                    for contact in contacts:
                        file.write(
                            f"{contact.get_first_name()};{contact.get_last_name()};{contact.get_phone_number()};{contact.get_email()};\n")

            elif format_selected == "VCF":
                with open(file_path, "w", encoding="utf-8") as file:
                    for contact in contacts:
                        file.write(f"BEGIN:VCARD\n")
                        file.write(f"VERSION:3.0\n")
                        file.write(f"N:{contact.get_last_name()};{contact.get_first_name()};;;\n")
                        file.write(f"FN:{contact.get_first_name()} {contact.get_last_name()}\n")
                        file.write(f"TEL;TYPE=CELL:{contact.get_phone_number()}\n")
                        file.write(f"EMAIL;TYPE=WORK:{contact.get_email()}\n")
                        file.write(f"END:VCARD\n")

            QMessageBox.information(None, "Успех", f"Контакты успешно экспортированы в формате {format_selected}")

        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Не удалось экспортировать контакты: {e}")

    else:
        QMessageBox.critical(None, "Ошибка", "Не выбрано место сохранения")

def import_contacts():
    pass


save_path = os.environ.get('LOCALAPPDATA')
save_path = get_and_check_path(save_path)
print(f'log: loadsaver: 41 line (path) - {save_path}')