import json
from typing import Dict, Any


class Customer:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            # Один аргумент - может быть словарем или JSON строкой
            if isinstance(args[0], str):
                # JSON строка
                try:
                    data = json.loads(args[0])
                    self.__init_from_dict(data)
                except json.JSONDecodeError:
                    raise ValueError("Некорректный JSON формат")
            elif isinstance(args[0], dict):
                # Словарь
                self.__init_from_dict(args[0])
            else:
                raise ValueError("Не поддерживаемый тип аргумента")
        elif len(args) == 5:
            # Обычное создание с 5 позиционными аргументами
            self.__validate_and_init(args[0], args[1], args[2], args[3], args[4])
        elif kwargs:
            # Создание из именованных параметров
            self.__init_from_kwargs(kwargs)
        else:
            raise ValueError("Неверное количество аргументов")

    def __init_from_dict(self, data: Dict[str, Any]):
        """Инициализация из словаря"""
        required_fields = ['customer_id', 'name', 'address', 'phone', 'contact_person']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Отсутствуют обязательные поля: {missing_fields}")

        self.__validate_and_init(
            data['customer_id'],
            data['name'],
            data['address'],
            data['phone'],
            data['contact_person']
        )

    def __init_from_kwargs(self, kwargs: Dict[str, Any]):
        """Инициализация из именованных параметров"""
        required_fields = ['customer_id', 'name', 'address', 'phone', 'contact_person']
        missing_fields = [field for field in required_fields if field not in kwargs]
        if missing_fields:
            raise ValueError(f"Отсутствуют обязательные поля: {missing_fields}")

        self.__validate_and_init(
            kwargs['customer_id'],
            kwargs['name'],
            kwargs['address'],
            kwargs['phone'],
            kwargs['contact_person']
        )

    def __validate_and_init(self, customer_id, name, address, phone, contact_person):
        """Общая валидация и инициализация полей"""
        self.__validate_customer_id(customer_id)
        self.__validate_string_field(name, "Наименование заказчика", 2)
        self.__validate_string_field(address, "Адрес", 5)
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
    def __validate_string_field(value, field_name, min_length=1):
        if not isinstance(value, str):
            raise ValueError(f"{field_name} должен быть строкой")
        if not value.strip():
            raise ValueError(f"{field_name} не может быть пустым")
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} должен содержать минимум {min_length} символов")

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
        # Используем универсальную валидацию для базовых проверок
        Customer.__validate_string_field(contact_person, "Контактное лицо", 2)

        # Дополнительная проверка на имя и фамилию
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
        self.__validate_string_field(name, "Наименование заказчика", 2)
        self.__name = name

    def set_address(self, address):
        self.__validate_string_field(address, "Адрес", 5)
        self.__address = address

    def set_phone(self, phone):
        self.__validate_phone(phone)
        self.__phone = phone

    def set_contact_person(self, contact_person):
        self.__validate_contact_person(contact_person)
        self.__contact_person = contact_person

    def __str__(self):
        return (f"Customer: ID={self.__customer_id}, Name='{self.__name}', "
                f"Phone='{self.__phone}', Contact='{self.__contact_person}'")