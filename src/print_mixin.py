class PrintMixin:
    """Миксин для логирования создания объектов с выводом в консоль."""

    def __init__(self, *args):
        super().__init__(*args)
        print(f"{self.__class__.__name__}{args}")
