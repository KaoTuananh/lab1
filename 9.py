import json
from typing import Dict, Any

class CustomerShort:
    """Базовый класс с краткой информацией о заказчике"""
    def __init__(self, customer_id: int, name: str, phone: str):

        self._validate_customer_id(customer_id)
        self._validate_name(name, "name")
        self._validate_phone(phone)

        self.__customer_id = customer_id
        self.__name = name
        self.__phone = phone

    # Статические методы валидации
    @staticmethod
    def _validate_customer_id(customer_id):
        """Валидация ID клиента"""
        if not isinstance(customer_id, int):
            raise ValueError("Customer ID должен быть целым числом")
        if customer_id <= 0:
            raise ValueError("Customer ID должен быть положительным числом")

    @staticmethod
    def _validate_name(name, field_name):
        """Валидация наименования заказчика"""
        if not isinstance(name, str):
            raise ValueError(f"{field_name} должен быть строкой")
        if not name.strip():
            raise ValueError(f"{field_name} не может быть пустым")
        if len(name.strip()) < 2:
            raise ValueError(f"{field_name} должен содержать минимум 2 символа")

    @staticmethod
    def _validate_phone(phone):
        """Валидация телефона"""
        if not isinstance(phone, str):
            raise ValueError("Телефон должен быть строкой")
        # Убираем пробелы, скобки, дефисы для проверки
        clean_phone = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        if not clean_phone.isdigit():
            raise ValueError("Телефон должен содержать только цифры и допустимые символы")
        if len(clean_phone) < 5:
            raise ValueError("Телефон должен содержать минимум 5 цифр")

    # Геттеры
    def get_customer_id(self) -> int:
        return self.__customer_id

    def get_name(self) -> str:
        return self.__name

    def get_phone(self) -> str:
        return self.__phone

    def to_string(self) -> str:
        return f"ID: {self.__customer_id}, Название: {self.__name}, Тел: {self.__phone}"

    # Строковые представления
    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return f"CustomerShort(customer_id={self.__customer_id}, name='{self.__name}', phone='{self.__phone}')"

    # Методы сравнения
    def __eq__(self, other) -> bool:
        if not isinstance(other, CustomerShort):
            return False
        return (self.__customer_id == other.__customer_id and
                self.__name == other.__name and
                self.__phone == other.__phone)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


class Customer(CustomerShort):

    def __init__(self, *args, **kwargs):

        if len(args) == 1:
            # Обработка единичного аргумента
            data = self._parse_single_arg(args[0])
            self._init_from_data(data)
        elif len(args) == 5:
            # Обычное создание
            self._init_from_data({
                'customer_id': args[0],
                'name': args[1],
                'address': args[2],
                'phone': args[3],
                'contact_person': args[4]
            })
        elif kwargs:
            # Создание из именованных параметров
            self._init_from_data(kwargs)
        else:
            raise ValueError("Неверное количество аргументов")

    def _parse_single_arg(self, arg):
        """Обработка единичного аргумента"""
        if isinstance(arg, str):
            try:
                return json.loads(arg)
            except json.JSONDecodeError:
                raise ValueError("Некорректный JSON формат")
        elif isinstance(arg, dict):
            return arg
        else:
            raise ValueError("Не поддерживаемый тип аргумента")

    def _init_from_data(self, data: Dict[str, Any]):
        """Инициализация из данных"""
        # Проверка обязательных полей
        required_fields = ['customer_id', 'name', 'address', 'phone', 'contact_person']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Отсутствуют обязательные поля: {missing_fields}")

        # Валидация дополнительных полей
        self._validate_address(data['address'])
        self._validate_contact_person(data['contact_person'])

        # Вызов конструктора родительского класса
        super().__init__(
            data['customer_id'],
            data['name'],
            data['phone']
        )

        self.__address = data['address']
        self.__contact_person = data['contact_person']

    @staticmethod
    def _validate_address(address):
        """Валидация адреса"""
        if not isinstance(address, str):
            raise ValueError("Адрес должен быть строкой")
        if not address.strip():
            raise ValueError("Адрес не может быть пустым")
        if len(address.strip()) < 5:
            raise ValueError("Адрес должен содержать минимум 5 символов")

    @staticmethod
    def _validate_contact_person(contact_person):
        """Валидация контактного лица"""
        if not isinstance(contact_person, str):
            raise ValueError("Контактное лицо должно быть строкой")
        if not contact_person.strip():
            raise ValueError("Контактное лицо не может быть пустым")
        if len(contact_person.strip()) < 2:
            raise ValueError("Контактное лицо должно содержать минимум 2 символа")
        if len(contact_person.strip().split()) < 2:
            raise ValueError("Контактное лицо должно содержать имя и фамилию")

    # Геттеры для дополнительных полей
    def get_address(self) -> str:
        return self.__address

    def get_contact_person(self) -> str:
        return self.__contact_person

    # Сеттеры с валидацией
    def set_address(self, address):
        self._validate_address(address)
        self.__address = address

    def set_contact_person(self, contact_person):
        self._validate_contact_person(contact_person)
        self.__contact_person = contact_person

    # Переопределенные методы
    def to_string(self) -> str:
        base_string = super().to_string()
        return f"{base_string}, Адрес: {self.__address}, Контакт: {self.__contact_person}"


    def to_short_version(self) -> CustomerShort:
        return CustomerShort(
            self.get_customer_id(),
            self.get_name(),
            self.get_phone()
        )

    # Строковые представления
    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return (f"Customer(customer_id={self.get_customer_id()}, name='{self.get_name()}', "
                f"address='{self.__address}', phone='{self.get_phone()}', "
                f"contact_person='{self.__contact_person}')")

    # Методы сравнения
    def __eq__(self, other) -> bool:
        if not isinstance(other, Customer):
            return False
        return (super().__eq__(other) and
                self.__address == other.__address and
                self.__contact_person == other.__contact_person)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    # Статические фабричные методы
    @classmethod
    def from_json(cls, json_str: str) -> 'Customer':
        """Создание заказчика из JSON строки"""
        return cls(json_str)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Customer':
        """Создание заказчика из словаря"""
        return cls(data)