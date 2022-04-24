from typing import Callable

from model.Stock import Stock
from model.fact_providers.StockFromFileProvider import StockFromFileProvider


class SpyStockFromFileProvider(StockFromFileProvider):
    argv: list[str] = None
    _on_get_stocks: Callable[[], list[Stock]]

    def __init__(self, on_get_stocks: Callable[[], list[Stock]]):
        self._on_get_stocks = on_get_stocks

    def get_stocks(self) -> list[Stock]:
        return self._on_get_stocks()

    def parse_args(self, argv: list[str]):
        self.argv = argv
