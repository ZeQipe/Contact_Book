from core.contact.contact import Contact


class ContainerContact:
    def __init__(self):
        self.__contacts = []
        self.__count = 0

    def get_count(self):
        return self.__count

    def get_contacts(self):
        return self.__contacts

    def add_contact(self, contact_data):
        contact = Contact(contact_data[0], contact_data[1], contact_data[2], contact_data[3])
        self.__contacts.append(contact)
        self.__count += 1

    def remove_contact(self, contact):
        if contact in self.__contacts:
            index = self.__contacts.index(contact)
            self.__contacts.pop(index)

    def search_contacts(self, keyword):
        results = []
        for contact in self.__contacts:
            if keyword.lower() in f"{contact.first_name} {contact.last_name}".lower():
                results.append(contact)
        return results

    def edit_contact(self, contact, new_value_data):
        if contact in self.__contacts:
            contact.set_first_name(new_value_data[0])
            contact.set_last_name(new_value_data[1])
            contact.set_phone_number(new_value_data[2])
            contact.set_email(new_value_data[3])
