class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__email = email

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, value):
        self.__first_name = value

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, value):
        self.__last_name = value

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, value):
        self.__phone_number = value

    def get_email(self):
        return self.__email

    def set_email(self, value):
        self.__email = value

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}"
