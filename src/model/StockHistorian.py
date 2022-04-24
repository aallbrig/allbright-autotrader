from datetime import date

from src.model.Stock import Stock
from src.model.StockDaySummary import StockDaySummary


class StockHistorian:
    _stock: Stock
    _stock_history: list[StockDaySummary]

    def __init__(self, stock: Stock):
        self._stock = stock

    def discover_history(self, start: date = date.today(), end: date = date.today()) -> list[StockDaySummary]:
        pass
