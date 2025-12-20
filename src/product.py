from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Класс, представляющий товар с его основными характеристиками."""

    def __init__(self, name, description, price, quantity):
        """Инициализирует экземпляр продукта."""
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        elif quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        """Метод для создания или обновления продукта."""

        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if not products_list:
            return cls(name, description, price, quantity)

        for existing_product in products_list:
            if existing_product.name == name:
                existing_product.quantity += quantity
                if price > existing_product.price:
                    existing_product.price = price
                return existing_product

        return cls(name, description, price, quantity)

    def __str__(self):
        """Строковое представление категории."""

        return f"{self.name}, {self._BaseProduct__price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        """Возвращает строковое представление объекта для целей отладки и логирования."""
        return str(self)

    def __add__(self, other):
        """Определяет сложение двух продуктов (по общей стоимости)."""
        if isinstance(other, Product):
            return self._BaseProduct__price * self.quantity + other._BaseProduct__price * other.quantity
        else:
            raise TypeError("Операция поддерживается только для объектов типа Product")

    @property
    def price(self):
        """Геттер для цены продукта."""
        return self._BaseProduct__price

    @price.setter
    def price(self, value):
        """Сеттер для цены продукта с валидацией."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self._BaseProduct__price:
            user_input = input(f"Цена понижается с {self._BaseProduct__price} до {value}. Подтвердить (y/n)? ")
            if user_input.lower() != "y":
                print("Изменение цены отменено")
                return

        self._BaseProduct__price = value


class Smartphone(Product):
    """Класс, представляющий смартфон как товар в ассортименте."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализирует экземпляр смартфона"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """
        Определяет логику сложения двух смартфонов.
        Сложение возможно только между объектами класса Smartphone.
        """

        if type(other) is not Smartphone:
            raise TypeError("Нельзя складывать товары разных категорий")
        return super().__add__(other)


class LawnGrass(Product):
    """Класс, представляющий газонную траву как товар в ассортименте."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализирует экземпляр газонной травы."""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """
        Определяет логику сложения двух упаковок газонной травы.
        Сложение возможно только между объектами класса LawnGrass.
        """

        if type(other) is not LawnGrass:
            raise TypeError("Нельзя складывать товары разных категорий")
        return super().__add__(other)
