from models.Stock import Stock
from models.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider
import yfinance as yf


class YahooFinanceStockInfoProvider(ThirdPartyStockInfoProvider):
    def __init__(self, stock_picks=None):
        super().__init__(stock_picks)

    @staticmethod
    def _map_stock_to_finance_data(stock_picks: list[Stock]):
        return [yf.Ticker(stock_pick.symbol()) for stock_pick in stock_picks]

    def retrieve_stock_info(self):
        return self.get_yahoo_info()

    def get_yahoo_info(self):
        return self._map_stock_to_finance_data(self._stock_picks)
