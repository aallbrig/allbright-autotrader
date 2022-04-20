from yfinance import Ticker

from src.model.Stock import Stock
from src.model.StockInfoReport import StockInfoReport
from src.model.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider
import yfinance as yf


class YahooFinanceStockInfoProvider(ThirdPartyStockInfoProvider):
    _local_cache: dict[Stock, Ticker]
    _ticker_to_stock_cache: dict[Ticker, Stock]

    def __init__(self, stock_picks: list[Stock] = None):
        super().__init__(stock_picks)
        self._local_cache = {}
        self._ticker_to_stock_cache = {}

    def retrieve_stock_info(self) -> list[StockInfoReport]:
        return self._map_stock_to_stock_info_report(self._get_yahoo_data(self._stock_picks))

    def _get_yahoo_data(self, stock_picks: list[Stock]) -> list[Ticker]:
        return [self._map_stock_to_yahoo_ticker(stock_pick) for stock_pick in stock_picks]

    def _generate_stock_info_report(self, yahoo_stock_data: Ticker):
        return StockInfoReport(self._ticker_to_stock_cache[yahoo_stock_data])

    def _map_stock_to_stock_info_report(self, yahoo_data: list[Ticker]) -> list[StockInfoReport]:
        return [self._generate_stock_info_report(yahoo_stock_data) for yahoo_stock_data in yahoo_data]

    def _map_stock_to_yahoo_ticker(self, stock_pick: Stock) -> Ticker:
        if stock_pick not in self._local_cache.keys():
            yahoo_ticker = yf.Ticker(stock_pick.symbol())
            self._local_cache[stock_pick] = yahoo_ticker
            self._ticker_to_stock_cache[yahoo_ticker] = stock_pick

        return self._local_cache.get(stock_pick)
