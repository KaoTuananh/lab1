class CustomerShort:
    """Класс с краткой информацией о заказчике"""

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