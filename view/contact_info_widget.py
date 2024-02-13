from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class ContactInfoWidget(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 16px;")  # Устанавливаем размер шрифта
        self.set_cursor()

    def set_contact_info(self, contact):
        if contact is not None:
            html_text = f"""
                    <html>
                    <body>
                        <p style="font-size: 22px;"><b>Контакт</b></p>
                        <p style="font-size: 18px; text-align: left;"><pre><b>   Имя и фамилия</b></pre></p>
                        <p style="text-align: left;"><pre>    {contact.get_first_name()} {contact.get_last_name()}</pre></p>
                        <p style="font-size: 18px; text-align: left;"><pre><b>   Номер телефона</b></pre></p>
                        <p style=" text-align: left;"><pre>    {contact.get_phone_number()}</a></pre></p>
                        <p style="font-size: 18px; text-align: left;"><pre><b>   Почтовый адрес</b></pre></p>
                        <p style="text-align: left;"><pre>    {contact.get_email()}</a></pre></p>
                    </body>
                    </html>
                """
        else:
            html_text = "<html><body><p><b>Контакт не выбран</b></p></body></html>"
        self.setText(html_text)

    def set_cursor(self):
        self.setCursor(Qt.PointingHandCursor)
