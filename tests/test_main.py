from io import StringIO
from unittest.mock import patch

import pytest

from main import Category, Product


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category():
    return Category("Телефоны", "Современные смартфоны премиум-класса")


def test_private_price_attribute(product):
    with pytest.raises(AttributeError):
        product.__price  # Исправлен на __price


def test_price_getter_setter_valid_value(product):
    product.price = 200000.0
    assert product.price == 200000.0


def test_price_setter_negative_value(product):
    with patch("sys.stdout", new=StringIO()) as fake_output:
        product.price = -100
        output = fake_output.getvalue().strip()
        assert output == "Цена не должна быть нулевая или отрицательная"
        assert product.price == 180000.0


def test_price_setter_zero_value(product):
    with patch("sys.stdout", new=StringIO()) as fake_output:
        product.price = 0
        output = fake_output.getvalue().strip()
        assert output == "Цена не должна быть нулевая или отрицательная"
        assert product.price == 180000.0


def test_price_reduction_confirmation_yes(product):
    with patch("builtins.input", side_effect=["y"]):
        product.price = 150000.0
        assert product.price == 150000.0


def test_price_reduction_confirmation_no(product):
    with patch("builtins.input", side_effect=["n"]), patch("sys.stdout", new=StringIO()) as fake_output:
        product.price = 150000.0
        output = fake_output.getvalue().strip()
        assert output == "Изменение цены отменено"
        assert product.price == 180000.0


def test_private_products_attribute(category):
    with pytest.raises(AttributeError):
        category.__products


def test_new_product_creation():
    data = {"name": "Test Product", "description": "Test Description", "price": 10000.0, "quantity": 10}

    product = Product.new_product(data)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 10000.0
    assert product.quantity == 10


def test_new_product_existing_duplicate():
    existing_product = Product("Duplicate Test", "Existing Desc", 5000.0, 5)
    duplicate_data = {"name": "Duplicate Test", "description": "New Desc", "price": 7000.0, "quantity": 10}

    updated_product = Product.new_product(duplicate_data, [existing_product])
    assert updated_product is existing_product
    assert updated_product.quantity == 15
    assert updated_product.price == 7000.0


def test_new_product_higher_price():
    existing_product = Product("Higher Price Test", "Desc", 5000.0, 5)
    higher_price_data = {"name": "Higher Price Test", "description": "New Desc", "price": 7000.0, "quantity": 10}

    updated_product = Product.new_product(higher_price_data, [existing_product])
    assert updated_product.price == 7000.0


def test_new_product_lower_price():
    existing_product = Product("Lower Price Test", "Desc", 7000.0, 5)
    lower_price_data = {"name": "Lower Price Test", "description": "New Desc", "price": 5000.0, "quantity": 10}

    updated_product = Product.new_product(lower_price_data, [existing_product])
    assert updated_product.price == 7000.0


def test_category_products_property(category):
    product1 = Product("Product A", "", 10000.0, 3)
    product2 = Product("Product B", "", 15000.0, 5)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = "Product A, 10000.0 руб. Остаток: 3 шт.\n" "Product B, 15000.0 руб. Остаток: 5 шт."

    assert category.products == expected_output


def test_empty_category_products(category):
    assert category.products == ""
