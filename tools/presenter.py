from view.other_window.other_message_window import show_error
from tools.loadsaver import save


def create_contact(window, dialog):
    first_name = dialog.first_name_input.text().strip()
    last_name = dialog.last_name_input.text().strip()
    phone = dialog.phone_input.text().strip()
    email = dialog.email_input.text().strip()

    if not first_name or not phone:
        show_error("Поля 'Имя' и 'Номер' обязательны для заполнения.")
        return

    for contact in window.container.get_contacts():
        if contact.get_first_name == first_name and contact.get_last_name == last_name:
            show_error("Контакт с таким именем и фамилией уже существует.")
            return

    data_collect = [first_name, last_name, phone, email]
    window.container.add_contact(data_collect)

    save(window.container)
    window.update_contacts_list()
    window.update_buttons_state(False)
    window.selected_contact = None
    window.contact_info_widget.setText("Выберите контакт для просмотра информации")

    dialog.accept()