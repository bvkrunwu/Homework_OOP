class Product:
    """Класс, представляющий товар с его основными характеристиками."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):

        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            user_input = input(f"Цена понижается с {self.__price} до {value}. Подтвердить (y/n)? ")
            if user_input.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = value


class Category:
    """
    Класс, представляющий категорию товаров.
    Содержит название, описание и приватный список товаров в категории.
    """

    product_count = 0

    def __init__(self, name, description, products=None):

        self.name = name
        self.description = description
        self.__products = []

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):

        if not self.__products:
            return ""

        product_lines = []
        for product in self.__products:
            line = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            product_lines.append(line)

        return "\n".join(product_lines)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
