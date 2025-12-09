from src.category import Category
from src.product import LawnGrass, Smartphone

if __name__ == "__main__":
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)  # Samsung Galaxy S23 Ultra
    print(smartphone1.description)  # 256GB, Серый цвет, 200MP камера
    print(smartphone1.price)  # 180000.0
    print(smartphone1.quantity)  # 5
    print(smartphone1.efficiency)  # 95.5
    print(smartphone1.model)  # S23 Ultra
    print(smartphone1.memory)  # 256
    print(smartphone1.color)  # Серый

    print(smartphone2.name)  # Iphone 15
    print(smartphone2.description)  # 512GB, Gray space
    print(smartphone2.price)  # 210000.0
    print(smartphone2.quantity)  # 8
    print(smartphone2.efficiency)  # 98.2
    print(smartphone2.model)  # 15
    print(smartphone2.memory)  # 512
    print(smartphone2.color)  # Gray space

    print(smartphone3.name)  # Xiaomi Redmi Note 11
    print(smartphone3.description)  # 1024GB, Синий
    print(smartphone3.price)  # 31000.0
    print(smartphone3.quantity)  # 14
    print(smartphone3.efficiency)  # 98.3
    print(smartphone3.model)  # Note 11
    print(smartphone3.memory)  # 1024
    print(smartphone3.color)  # Синий

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)  # Газонная трава
    print(grass1.description)  # Элитная трава для газона
    print(grass1.price)  # 500.0
    print(grass1.quantity)  # 20
    print(grass1.country)  # Россия
    print(grass1.germination_period)  # 7 дней
    print(grass1.color)  # Зеленый

    print(grass2.name)  # Газонная трава 2
    print(grass2.description)  # Выносливая трава
    print(grass2.price)  # 450.0
    print(grass2.quantity)  # 15
    print(grass2.country)  # США
    print(grass2.germination_period)  # 5 дней
    print(grass2.color)  # Темно-зеленый

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)  # 2580000.0

    grass_sum = grass1 + grass2
    print(grass_sum)  # 16750.0

    try:
        invalid_sum = smartphone1 + grass1  # Возникла ошибка TypeError при попытке сложения
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)  # 5

    try:
        category_smartphones.add_product("Not a product")  # Возникла ошибка TypeError при добавлении не продукта
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
