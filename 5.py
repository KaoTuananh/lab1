class Customer:
    def __init__(self, customer_id, name, address, phone, contact_person):
        # Валидация всех полей перед созданием объекта
        self.__validate_customer_id(customer_id)
        self.__validate_name(name)
        self.__validate_address(address)
        self.__validate_phone(phone)
        self.__validate_contact_person(contact_person)

        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__contact_person = contact_person

    # Статические методы валидации
    @staticmethod
    def __validate_customer_id(customer_id):
        if not isinstance(customer_id, int):
            raise ValueError("Customer ID должен быть целым числом")
        if customer_id <= 0:
            raise ValueError("Customer ID должен быть положительным числом")

    @staticmethod
    def __validate_name(name):
        if not isinstance(name, str):
            raise ValueError("Наименование заказчика должно быть строкой")
        if not name.strip():
            raise ValueError("Наименование заказчика не может быть пустым")
        if len(name.strip()) < 2:
            raise ValueError("Наименование заказчика должно содержать минимум 2 символа")

    @staticmethod
    def __validate_address(address):
        if not isinstance(address, str):
            raise ValueError("Адрес должен быть строкой")
        if not address.strip():
            raise ValueError("Адрес не может быть пустым")
        if len(address.strip()) < 5:
            raise ValueError("Адрес должен содержать минимум 5 символов")

    @staticmethod
    def __validate_phone(phone):
        if not isinstance(phone, str):
            raise ValueError("Телефон должен быть строкой")
        # Убираем пробелы, скобки, дефисы для проверки
        clean_phone = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        if not clean_phone.isdigit():
            raise ValueError("Телефон должен содержать только цифры и допустимые символы")
        if len(clean_phone) < 5:
            raise ValueError("Телефон должен содержать минимум 5 цифр")

    @staticmethod
    def __validate_contact_person(contact_person):
        if not isinstance(contact_person, str):
            raise ValueError("Контактное лицо должно быть строкой")
        if not contact_person.strip():
            raise ValueError("Контактное лицо не может быть пустым")
        if len(contact_person.strip()) < 2:
            raise ValueError("Контактное лицо должно содержать минимум 2 символа")
        # Проверяем, что есть хотя бы имя и фамилия (хотя бы 2 слова)
        if len(contact_person.strip().split()) < 2:
            raise ValueError("Контактное лицо должно содержать имя и фамилию")

    # Геттеры
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_contact_person(self):
        return self.__contact_person

    # Сеттеры с валидацией
    def set_customer_id(self, customer_id):
        self.__validate_customer_id(customer_id)
        self.__customer_id = customer_id

    def set_name(self, name):
        self.__validate_name(name)
        self.__name = name

    def set_address(self, address):
        self.__validate_address(address)
        self.__address = address

    def set_phone(self, phone):
        self.__validate_phone(phone)
        self.__phone = phone

    def set_contact_person(self, contact_person):
        self.__validate_contact_person(contact_person)
        self.__contact_person = contact_person