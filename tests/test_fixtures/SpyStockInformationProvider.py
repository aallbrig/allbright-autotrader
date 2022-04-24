from datetime import date
from typing import Callable

from model.Stock import Stock
from model.reports.StockDaySummary import StockDaySummary
from model.fact_providers.StockInformationProvider import StockInformationProvider
from model.reports.StockNowSummary import StockNowSummary


class SpyStockInformationProvider(StockInformationProvider):
    def map_info_source_to_stock_now_summary(self, stock: Stock) -> StockNowSummary:
        return self.on_map_stock_to_now_summary(stock)

    def retrieve_historic_data(self, stock: Stock, start_date: date, end_date: date) -> list[StockDaySummary]:
        pass

    def __init__(self, stocks: list[Stock] = None,
                 on_map_stock_to_now_summary: Callable[[Stock], StockNowSummary] = lambda _: StockNowSummary()):
        if stocks is None:
            stocks = []
        super().__init__(stocks)
        self.on_map_stock_to_now_summary = on_map_stock_to_now_summary
