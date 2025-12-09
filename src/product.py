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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Операция поддерживается только для объектов типа Product ")

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


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is not Smartphone:
            raise TypeError("Нельзя складывать товары разных категорий")
        return super().__add__(other)


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is not LawnGrass:
            raise TypeError("Нельзя складывать товары разных категорий")
        return super().__add__(other)
