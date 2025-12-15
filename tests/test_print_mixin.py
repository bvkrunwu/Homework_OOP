from src.product import LawnGrass, Product, Smartphone


def test_print_mixin(capsys):

    Product("Acer SHJ", "Монитор 27 дюймов, 2К", 250000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Acer SHJ', 'Монитор 27 дюймов, 2К', 250000.0, 8)"

    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        "90%",
        "Galaxy S23 Ultra",
        "256GB",
        "серый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"
    )

    LawnGrass(
        "Газонная трава Премиум",
        "Семена высокой всхожести, зелёный цвет",
        250.0,
        18,
        "Россия",
        "14–21 день",
        "зелёный",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass('Газонная трава Премиум', 'Семена высокой всхожести, зелёный цвет', 250.0, 18)"
    )
