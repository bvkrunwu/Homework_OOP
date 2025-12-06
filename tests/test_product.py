from io import StringIO
from unittest.mock import patch

import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_private_price_attribute(product):
    with pytest.raises(AttributeError):
        product.__price


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


def test_new_product_empty_list():
    data = {"name": "Solo Product", "description": "Solo Desc", "price": 3000.0, "quantity": 8}
    product = Product.new_product(data, [])
    assert product.name == "Solo Product"
    assert product.quantity == 8


def test_new_product_no_match_in_list():
    existing = Product("Other Product", "Desc", 1000.0, 2)
    new_data = {"name": "New Unique", "description": "Desc", "price": 2000.0, "quantity": 4}
    product = Product.new_product(new_data, [existing])
    assert product.name == "New Unique"
    assert product.quantity == 4
    assert product.price == 2000.0


def test_add_two_products():
    product_a = Product("A", "", 10000.0, 3)
    product_b = Product("B", "", 15000.0, 5)
    result = product_a + product_b
    assert result == 105000.0  # (10000×3) + (15000×5) = 30000 + 75000


def test_add_same_product():
    product_c = Product("C", "", 20000.0, 2)
    result = product_c + product_c
    assert result == 80000.0  # (20000×2) × 2 = 80000


def test_add_invalid_type(product):
    with pytest.raises(TypeError) as excinfo:
        _ = product + "invalid_object"
    assert "Операция поддерживается только для объектов типа Product" in str(excinfo.value)


def test_add_with_none(product):
    with pytest.raises(TypeError) as excinfo:
        _ = product + None
    assert "Операция поддерживается только для объектов типа Product" in str(excinfo.value)


def test_str_representation():
    product = Product("Widget", "Простая вещь", 999.99, 12)
    expected = "Widget, 999.99 руб. Остаток: 12 шт."
    assert str(product) == expected


def test_str_zero_quantity():
    product = Product("Out of Stock", "Нет в наличии", 500.0, 0)
    expected = "Out of Stock, 500.0 руб. Остаток: 0 шт."
    assert str(product) == expected


def test_str_large_quantity():
    product = Product("Bulk Item", "Много штук", 100.0, 1000)
    expected = "Bulk Item, 100.0 руб. Остаток: 1000 шт."
    assert str(product) == expected


def test_product_zero_price_initial():
    # Хотя setter запрещает ноль, __init__ может принять — проверим поведение
    product = Product("Free Item", "Бесплатный", 0.0, 10)
    with patch("sys.stdout", new=StringIO()) as fake_output:
        product.price = -1  # попытка изменить
        output = fake_output.getvalue().strip()
        assert output == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 0.0  # остаётся нулём


def test_product_negative_quantity_initial():
    """Тест: продукт может быть создан с отрицательным значением quantity."""
    product = Product("Negative Qty", "Странный товар", 100.0, -5)
    assert product.quantity == -5
    assert product.name == "Negative Qty"
    assert product.price == 100.0
    assert isinstance(product, Product)
