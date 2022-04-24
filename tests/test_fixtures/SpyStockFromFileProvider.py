from typing import Callable

from model.Stock import Stock
from model.fact_providers.StockFromFileProvider import StockFromFileProvider


class SpyStockFromFileProvider(StockFromFileProvider):
    def is_valid(self):
        return self._on_is_valid()

    argv: list[str] = None
    _on_get_stocks: Callable[[], list[Stock]]
    _on_get_stocks: Callable[[], bool]

    def __init__(self, on_get_stocks: Callable[[], list[Stock]], on_is_valid: Callable[[], bool] = lambda: True):
        self._on_get_stocks = on_get_stocks
        self._on_is_valid = on_is_valid

    def get_stocks(self) -> list[Stock]:
        return self._on_get_stocks()

    def parse_args(self, argv: list[str]):
        self.argv = argv
