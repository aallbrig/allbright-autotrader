from datetime import date

from model.Stock import Stock

from model.reports.StockDaySummary import StockDaySummary
from model.reports.StockNowSummary import StockNowSummary


class StockInformationProvider:
    _stock_picks: list[Stock]

    def __init__(self, stock_picks=None):
        if stock_picks is None:
            stock_picks = []
        self.set_stock_picks(stock_picks)

    def set_stock_picks(self, stock_picks: list[Stock]):
        self._stock_picks = stock_picks

    def retrieve_now_summary(self):
        [stock_pick.set_day_summary(self.map_info_source_to_stock_now_summary(stock_pick))
         for stock_pick in self._stock_picks]

    def map_info_source_to_stock_now_summary(self, stock: Stock) -> StockNowSummary:
        raise NotImplementedError("Please Implement this method")

    def retrieve_historic_data(self, stock: Stock, start_date: date, end_date: date) -> list[StockDaySummary]:
        raise NotImplementedError("Please Implement this method")
