from abc import ABC, abstractmethod


class AbstractEntity(ABC):
    """Общий абстрактный класс для сущностей.
    Выносит общие свойства классов Order и Category.
    """

    def __init__(self, entity_id=None):
        self.entity_id = entity_id

    @abstractmethod
    def calculate_total(self):
        """Метод для расчёта итоговой суммы сущности.
        Должен быть реализован в каждом наследнике.
        """
        pass


class Product(AbstractEntity):
    """Класс, представляющий товар."""

    def __init__(self, product_id, name, price_per_unit):
        super().__init__(entity_id=product_id)
        self.name = name
        self.price_per_unit = price_per_unit

    def calculate_total(self):
        """Возвращает цену за одну единицу товара."""
        return self.price_per_unit


class Order(AbstractEntity):
    """Класс, представляющий заказ.
    Содержит:
    - ссылку на товар (product)
    - количество купленного товара (quantity)
    - итоговую стоимость (total_cost)
    В заказе может быть указан только один товар.
    """

    def __init__(self, order_id, product, quantity):
        super().__init__(entity_id=order_id)
        self.product = product
        self.quantity = quantity
        self.total_cost = None

    def calculate_total(self):
        """Расчёт итоговой стоимости заказа:
        цена за единицу товара * количество.
        """
        self.total_cost = self.product.price_per_unit * self.quantity
        return self.total_cost

    def __repr__(self):
        return (
            f"Order(entity_id={self.entity_id}, "
            f"product={self.product.name}, "
            f"quantity={self.quantity}, "
            f"total_cost={self.total_cost})"
        )


class Category(AbstractEntity):
    """Класс, представляющий категорию товаров.
    Демонстрирует выделение общих свойств в AbstractEntity.
    """

    def __init__(self, category_id, name, description=""):
        super().__init__(entity_id=category_id)
        self.name = name
        self.description = description

    def calculate_total(self):
        """Для категории расчёт не определён (пример реализации).
        Может быть переопределён для специфических сценариев.
        """
        raise NotImplementedError(
            "Метод расчёта итоговой суммы не реализован " "для категории. Требуется дополнительная логика."
        )
