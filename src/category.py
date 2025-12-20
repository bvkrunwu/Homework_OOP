from src.product import Product


class Category:
    """
    Класс, представляющий категорию товаров.
    Содержит название, описание и приватный список товаров в категории.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация экземпляра категории"""

        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        """Добавляет товар в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    def get_products(self):
        """Возвращает список товаров в категории."""
        return self.__products

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.get_products())
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        """Геттер для приватного атрибута __products."""
        return self.__products

    def middle_price(self):
        """
        Вычисляет средний ценник всех товаров в категории.
        Если товаров нет, возвращает 0.
        """
        products = self.get_products()
        if not products:
            return 0

        total_price = sum(product.price for product in products)

        try:
            average_price = total_price / len(products)
            return average_price
        except ZeroDivisionError:
            return 0


class CategoryIterators:
    """Вспомогательный класс для итерации п товарам категории"""

    def __init__(self, category):
        """Инициализация итератора."""
        self.category = category
        self.index = 0

    def __iter__(self):
        """Возвращает сам себя как итератор."""
        return self

    def __next__(self):
        """Переходит к следующему элементу коллекции товаров."""
        if self.index >= len(self.category.products):
            raise StopIteration

        product = self.category.products[self.index]
        self.index += 1
        return product
