from PySide6.QtWidgets import QListWidgetItem, QMessageBox
from view.other_window.add_contact_window import AddDialogWindow
from view.other_window.edit_contact_window import EditDialogWindow
from view.other_window.other_message_window import approv_delete_window
from tools.presenter import *


def handle_search(window, text):
    filtered_contacts = [contact for contact in window.container.get_contacts() if
                         text.lower() in contact.get_first_name().lower() or text.lower() in contact.get_last_name().lower()]

    window.update_contacts_list(filtered_contacts)

    if len(filtered_contacts) == 0:
        window.contacts_list_widget.clear()
        empty_item = QListWidgetItem("Пусто. Добавьте свой первый контакт!")
        window.contacts_list_widget.addItem(empty_item)


def handle_add_contact(window):
    pass


def handle_select_contact(window):
    pass


def handle_edit_contact(window):
    pass


def handle_delete_button_click(window):
    pass


def handle_import_contacts(window):
    pass


def handle_export_contacts(window):
    pass