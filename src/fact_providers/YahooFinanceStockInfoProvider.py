from datetime import date

from yfinance import Ticker

from model.Stock import Stock
from model.reports.StockDaySummary import StockDaySummary
from model.fact_providers.StockInformationProvider import StockInformationProvider
import yfinance as yf

from model.reports.StockNowSummary import StockNowSummary


class YahooFinanceStockInfoProvider(StockInformationProvider):
    def map_info_source_to_stock_now_summary(self, stock: Stock) -> StockNowSummary:
        summary = StockNowSummary()
        # yahoo_ticker = self._get_yahoo_ticker(stock)
        # summary.current = yahoo_ticker.info['currentPrice']
        return summary

    def retrieve_historic_data(self, stock: Stock, start_date: date, end_date: date) -> list[StockDaySummary]:
        yahoo_ticker = self._get_yahoo_ticker(stock)
        yahoo_ticker.history(start=start_date, end=end_date)
        return []

    _local_cache: dict[Stock, Ticker]

    def __init__(self, stock_picks: list[Stock] = None):
        super().__init__(stock_picks)
        self._local_cache = {}
        self._ticker_to_stock_cache = {}

    def _get_yahoo_ticker(self, stock_pick) -> yf.Ticker:
        self._ensure_ticker_present(stock_pick)
        yahoo_ticker = self._local_cache[stock_pick]
        return yahoo_ticker

    def _ensure_ticker_present(self, stock_pick):
        if stock_pick not in self._local_cache.keys():
            yahoo_ticker = yf.Ticker(stock_pick.symbol())
            self._local_cache[stock_pick] = yahoo_ticker
