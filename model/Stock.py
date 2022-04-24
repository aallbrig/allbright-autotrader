class Stock:
    _symbol: str = None

    def __init__(self, symbol: str):
        self._symbol = symbol

    def symbol(self) -> str:
        return self._symbol
