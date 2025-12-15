from src.product import Product


class Category:
    """
    Класс, представляющий категорию товаров.
    Содержит название, описание и приватный список товаров в категории.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):

        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    def get_products(self):
        return self.__products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.get_products())
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        return self.__products


class CategoryIterators:
    """Вспомогательный класс для итерации п товарам категории"""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.category.products):
            raise StopIteration

        product = self.category.products[self.index]
        self.index += 1
        return product
