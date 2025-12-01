import pytest

from main import Category, Product


@pytest.fixture()
def product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )

@pytest.fixture()
def another_product():
    return Product(
        name="iPhone 15 Pro Max",
        description="512GB, Space Black, LiDAR camera",
        price=210000.0,
        quantity=8
    )

@pytest.fixture()
def product_list(product, another_product):
    return [product, another_product]

@pytest.fixture()
def category(product_list):
    return Category(
        name="Телефоны",
        description="Современные смартфоны премиум-класса",
        products=product_list
    )