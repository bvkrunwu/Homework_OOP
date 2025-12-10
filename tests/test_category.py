import pytest

from src.category import Category, CategoryIterators
from src.product import Product


@pytest.fixture
def category():
    # Обнуляем счётчик перед каждым тестом
    Category.product_count = 0
    return Category("Электроника", "Категория электроники")


def test_create_category(category):
    assert category.name == "Электроника"
    assert category.description == "Категория электроники"


def test_add_product(category):
    product = Product("Смартфон", "Новый смартфон", 10000.0, 10)
    category.add_product(product)
    assert category.products == "Смартфон, 10000.0 руб. Остаток: 10 шт."


def test_add_multiple_products(category):
    product1 = Product("Смартфон", "Новый смартфон", 10000.0, 10)
    product2 = Product("Ноутбук", "Легкий ноутбук", 20000.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    expected_output = "Смартфон, 10000.0 руб. Остаток: 10 шт.\nНоутбук, 20000.0 руб. Остаток: 5 шт."
    assert category.products == expected_output


def test_empty_category(category):
    assert category.products == ""


def test_empty_str_representation(category):
    try:
        result = str(category)
        assert "Электроника" in result
        assert "0 шт." in result
    except Exception as e:
        pytest.fail(f"__str__ для пустой категории вызвал ошибку: {e}")


def test_iterator_single_product(category):
    single_product = Product("Смартфон", "Новый смартфон", 10000.0, 10)
    category.add_product(single_product)
    iterator = CategoryIterators(category)

    first_char = next(iterator)
    assert isinstance(first_char, str)
    assert first_char == "С"

    all_chars = [first_char]
    while True:
        try:
            char = next(iterator)
            all_chars.append(char)
        except StopIteration:
            break

    expected_string = "Смартфон, 10000.0 руб. Остаток: 10 шт."
    assert "".join(all_chars) == expected_string


def test_iterator_multiple_products(category):
    product1 = Product("Смартфон", "Новый смартфон", 10000.0, 10)
    product2 = Product("Ноутбук", "Легкий ноутбук", 20000.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    iterator = CategoryIterators(category)

    first_char = next(iterator)
    all_chars = [first_char]

    while True:
        try:
            char = next(iterator)
            all_chars.append(char)
        except StopIteration:
            break

    expected_string = "Смартфон, 10000.0 руб. Остаток: 10 шт.\nНоутбук, 20000.0 руб. Остаток: 5 шт."
    assert "".join(all_chars) == expected_string


def test_iterator_empty_category():
    empty_category = Category("Пустая", "")
    iterator = CategoryIterators(empty_category)
    with pytest.raises(StopIteration):
        next(iterator)


def test_add_product_invalid_type_catches_typeerror(category):
    """Проверка, что добавление не‑продукта вызывает TypeError и не увеличивает счётчик."""
    initial_count = Category.product_count  # Запоминаем начальное значение
    invalid_objects = ["Не продукт", 123, None, [], {}, lambda: None]

    for obj in invalid_objects:
        try:
            category.add_product(obj)
            assert False, f"Не возникло TypeError при добавлении {type(obj).__name__}"
        except TypeError as e:
            assert "Можно добавлять только объекты класса Product или его наследников" in str(e)

    # Убедимся, что счётчик не изменился и список пуст
    assert Category.product_count == initial_count
    assert len(category.get_products()) == 0


def test_add_product_none_catches_typeerror(category):
    """Проверка, что None вызывает TypeError."""
    try:
        category.add_product(None)
        assert False, "Не возникло TypeError при добавлении None"
    except TypeError as e:
        assert "Можно добавлять только объекты класса Product или его наследников" in str(e)


def test_add_product_string_catches_typeerror(category):
    """Проверка, что строка вызывает TypeError."""
    try:
        category.add_product("Это не продукт")
        assert False, "Не возникло TypeError при добавлении строки"
    except TypeError as e:
        assert "Можно добавлять только объекты класса Product или его наследников" in str(e)
