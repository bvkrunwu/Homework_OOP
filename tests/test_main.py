from main import Category, Product


def test_product_initialization(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_category_initialization(category):
    assert category.name == "Телефоны"
    assert category.description == "Современные смартфоны премиум-класса"
    assert isinstance(category.products, list)
    assert all(isinstance(item, Product) for item in category.products)

def test_product_count(category):
    initial_product_count = Category.product_count
    new_products = [Product("New Phone", "", 100000.0, 3)]
    Category("Ноутбуки", "Лучшие ноутбуки", new_products)
    assert Category.product_count == initial_product_count + len(new_products)

def test_category_count(category):
    initial_category_count = Category.category_count
    Category("Планшеты", "Популярные планшеты", [])
    assert Category.category_count == initial_category_count + 1

def test_reset_counts():
    original_category_count = Category.category_count
    original_product_count = Category.product_count
    Category("Игровые консоли", "Новые игровые приставки", [])
    assert Category.category_count == original_category_count + 1
    assert Category.product_count == original_product_count

def test_integrated_scenario():
    # Принудительная очистка статических переменных перед тестом
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Galaxy Tab S8", "Таблетка Samsung", 80000.0, 10)
    p2 = Product("iPad Air", "Apple планшет", 70000.0, 15)
    cat1 = Category("Планшеты", "Различные модели планшетов", [p1, p2])
    assert cat1.name == "Планшеты"
    assert len(cat1.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2

    p3 = Product("MacBook Pro", "Ноутбук Apple", 200000.0, 5)
    cat2 = Category("Ноутбуки", "Производительные ноутбуки", [p3])
    assert cat2.name == "Ноутбуки"
    assert len(cat2.products) == 1
    assert Category.category_count == 2
    assert Category.product_count == 3