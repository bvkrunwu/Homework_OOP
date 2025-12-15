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
    # Сравниваем не строку, а проверяем наличие продукта в списке
    assert len(category.products) == 1
    assert category.products[0] == product


def test_add_multiple_products(category):
    product1 = Product("Смартфон", "Новый смартфон", 10000.0, 10)
    product2 = Product("Ноутбук", "Легкий ноутбук", 20000.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert len(category.products) == 2
    assert category.products[0] == product1
    assert category.products[1] == product2


def test_empty_category(category):
    # Если products — список, то он должен быть пустым, а не строкой
    assert len(category.products) == 0


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

    first_product = next(iterator)
    assert isinstance(first_product, Product)
    assert first_product.name == "Смартфон"

    all_products = [first_product]
    while True:
        try:
            product = next(iterator)
            all_products.append(product)
        except StopIteration:
            break

    assert len(all_products) == 1
    assert all_products[0] == single_product


def test_iterator_multiple_products(category):
    product1 = Product("Смартфон", "Новый смартфон", 10000.0, 10)
    product2 = Product("Ноутбук", "Легкий ноутбук", 20000.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    iterator = CategoryIterators(category)

    products_list = []
    while True:
        try:
            product = next(iterator)
            products_list.append(product)
        except StopIteration:
            break

    assert len(products_list) == 2
    assert products_list[0] == product1
    assert products_list[1] == product2


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
    assert len(category.products) == 0


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
