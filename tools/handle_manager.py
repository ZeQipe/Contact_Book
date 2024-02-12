from PySide6.QtWidgets import QListWidgetItem, QMessageBox
from view.other_window.add_contact_window import AddDialogWindow
from view.other_window.edit_contact_window import EditDialogWindow
from view.other_window.other_message_window import approv_delete_window
from tools.presenter import *
from tools.loadsaver import export_contacts


def handle_search(window, text):
    filtered_contacts = [contact for contact in window.container.get_contacts() if
                         text.lower() in contact.get_first_name().lower() or text.lower() in contact.get_last_name().lower()]

    window.update_contacts_list(filtered_contacts)

    if len(filtered_contacts) == 0:
        window.contacts_list_widget.clear()
        empty_item = QListWidgetItem("Пусто. Добавьте свой первый контакт!")
        window.contacts_list_widget.addItem(empty_item)


def handle_add_contact(window):
    dialog = AddDialogWindow()
    dialog.save_clicked.connect(lambda: create_contact(window, dialog))
    dialog.exec_()


def handle_select_contact(window):
    window.update_buttons_state(True)
    window.select_contact = window.contacts_list_widget.current_contact
    window.contact_info_widget.set_contact_info(window.select_contact)


def handle_edit_contact(window):
    dialog = EditDialogWindow(window.select_contact)
    dialog.save_clicked.connect(lambda: edit_contact(window, dialog))
    dialog.exec_()


def handle_delete_button_click(window):
    msg_box = approv_delete_window(window.select_contact)

    if msg_box == QMessageBox.Ok:
        delete_contact(window)


def handle_import_contacts(window):
    show_error('Функция в разработке')


def handle_export_contacts(window):
    export_contacts(window.container.get_contacts())
