from view.other_window.other_message_window import show_error
import os
from PySide6.QtWidgets import QFileDialog, QMessageBox


def export_contacts(contacts):
    file_path, _ = QFileDialog.getSaveFileName(None, "Выберите место сохранения", "",
                                               "CSV Files (*.csv);;VCF Files (*.vcf)")

    if file_path:
        try:
            format_selected = "CSV" if file_path.endswith(".csv") else "VCF"

            if format_selected == "CSV":
                export_csv(contacts, file_path)

            elif format_selected == "VCF":
                export_vcf(contacts, file_path)

            QMessageBox.information(None, "Успех", f"Контакты успешно экспортированы в формате {format_selected}")

        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Не удалось экспортировать контакты: {e}")

    else:
        QMessageBox.critical(None, "Ошибка", "Не выбрано место сохранения")


def export_vcf(contacts, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(f"BEGIN:VCARD\n")
            file.write(f"VERSION:3.0\n")
            file.write(f"N:{contact.get_last_name()};{contact.get_first_name()};;;\n")
            file.write(f"FN:{contact.get_first_name()} {contact.get_last_name()}\n")
            file.write(f"TEL;TYPE=CELL:{contact.get_phone_number()}\n")
            file.write(f"EMAIL;TYPE=WORK:{contact.get_email()}\n")
            file.write(f"END:VCARD\n")


def export_csv(contacts, file_path):
    with open(file_path, "w", encoding="utf-8-sig") as file:
        file.write('Name;SurName;Number Phone; EMail Address;\n')
        for contact in contacts:
            file.write(
                f"{contact.get_first_name()};{contact.get_last_name()};{contact.get_phone_number()};{contact.get_email()};\n")


def import_contacts(window):
    file_path, _ = QFileDialog.getOpenFileName(None, "Выберите файл для импорта", "",
                                               "CSV Files (*.csv);;VCF Files (*.vcf)")

    if file_path:
        _, file_extension = os.path.splitext(file_path)

        if file_extension.lower() in ['.csv', '.vcf']:
            try:
                if file_extension.lower() == '.csv':
                    contacts = parse_csv_file(file_path)
                else:
                    contacts = parse_vcf_file(file_path)

                for contact_data in contacts:
                    window.container.add_contact(contact_data)

                QMessageBox.information(None, "Импорт контактов", "Контакты успешно импортированы!")

            except Exception as e:
                show_error(f"Ошибка чтения файла {str(e)}")
                print(str(e))
        else:
            show_error("Неверный формат файла\nПожалуйста, выберите файл с расширением CSV или VCF.")
    else:
        return


def parse_csv_file(file_path):
    contacts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_data = file.read()
        lines = csv_data.strip().split('\n')

    for line in lines[1::]:
        data = [item.strip() for item in line.split(';')]
        if len(data) > 3:
            first_name = data[0]
            last_name = data[1]
            phone_number = data[2]
            email = data[3]

            if not phone_number.replace('+', '').isdigit():
                print(f"Ошибка в строке {line}: номер телефона содержит недопустимые символы")
                continue

            contacts.append([first_name, last_name, phone_number, email])
        else:
            print("Ошибка в формате данных:", data)

    return contacts


def parse_vcf_file(file_path):
    contacts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        vcf_data = file.read()
        lines = vcf_data.strip().split('\n')

    i = 0
    while i < len(lines):
        first_name = ''
        last_name = ''
        phone_number = ''
        email = ''

        if lines[i].startswith('BEGIN:VCARD'):
            i += 1
            while i < len(lines) and not lines[i].startswith('BEGIN:VCARD'):
                line = lines[i].strip()

                if line.startswith('N:'):
                    name_parts = line.split(':')[1].split(';')
                    if len(name_parts) > 0:
                        last_name = name_parts[0].strip()
                    if len(name_parts) > 1:
                        first_name = name_parts[1].strip()

                elif line.startswith('FN:'):
                    full_name = line.split(':')[1].strip()
                    if not first_name:
                        first_name = full_name.split()[0]
                    if not last_name:
                        last_name = ' '.join(full_name.split()[1:])

                elif line.startswith('TEL;'):
                    phone_number = line.split(':')[1].strip()

                elif line.startswith('EMAIL;'):
                    email = line.split(':')[1].strip()

                i += 1
            contacts.append([first_name, last_name, phone_number, email])

        else:
            i += 1

    return contacts

def extract_vcard_value(vcard, key):
    start_index = vcard.find(key + ':') + len(key + ':')
    end_index = vcard.find('\n', start_index)
    return vcard[start_index:end_index].strip()


def parse_contact_info(contact_row):
    if 'first_name' in contact_row and 'phone_number' in contact_row:
        contact_info = [contact_row['first_name'], contact_row.get('last_name', ''),
                        contact_row['phone_number'], contact_row.get('email', '')]
        return contact_info
    else:
        return None
