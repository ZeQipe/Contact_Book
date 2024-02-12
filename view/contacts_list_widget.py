from PySide6 import QtGui
from PySide6.QtWidgets import QListWidget
from PySide6.QtCore import Qt, Signal
from core.contact.contact import Contact


class ContactsListWidget(QListWidget):
    contact_selected = Signal(Contact)
    current_contact = None

    def __init__(self):
        super().__init__()
        self.itemClicked.connect(self.on_item_clicked)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.count() == 0:
            painter = QtGui.QPainter(self.viewport())
            painter.setPen(QtGui.QColor(Qt.gray))
            painter.drawText(self.viewport().rect(), Qt.AlignCenter, "Пусто. Добавьте свой первый контакт!")

    def on_item_clicked(self, item):
        contact = item.data(Qt.UserRole)
        if contact:
            ContactsListWidget.current_contact = contact
            self.contact_selected.emit(contact)
