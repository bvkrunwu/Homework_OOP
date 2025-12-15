from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для представления продуктов"""

    def __init__(self, name, description, price, quantity):
        """Инициализирует экземпляр продукта."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Метод для создания или обновления продукта."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Определяет сложение двух продуктов (по общей стоимости)."""
        pass

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены продукта."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер для цены продукта с валидацией."""
        pass
