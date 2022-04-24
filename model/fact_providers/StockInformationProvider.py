from datetime import date

from model.Stock import Stock


from model.StockDaySummary import StockDaySummary
from model.StockInfoReport import StockInfoReport


class StockInformationProvider:
    _stock_picks: list[Stock]

    def __init__(self, stock_picks=None):
        if stock_picks is None:
            stock_picks = []
        self.set_stock_picks(stock_picks)

    def set_stock_picks(self, stock_picks: list[Stock]):
        self._stock_picks = stock_picks

    def retrieve_stock_info(self) -> list[StockInfoReport]:
        raise NotImplementedError("Please Implement this method")

    def retrieve_historic_data(self, stock: Stock, start_date: date, end_date: date) -> list[StockDaySummary]:
        raise NotImplementedError("Please Implement this method")
