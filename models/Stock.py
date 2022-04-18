# class FactDiscoveryRequest:
# stocks: list[StockInterface]
# pass

# class StockFacts:
# pass

# class FactDiscoveryResult:
# facts: list[StockFacts]
# pass

# Do stocks know how to get information about themselves?
class Stock:
    _symbol = None

    def __init__(self, symbol: str):
        self._symbol = symbol

    def symbol(self) -> str:
        return self._symbol
