import string

from models.Stock import Stock
from models.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider


class TestThirdPartyStockInfoProvider(ThirdPartyStockInfoProvider):
    def __init__(self, list_of_stock_tickers: list[string]):
        stocks = []
        for stock_ticker in list_of_stock_tickers:
            stocks.append(Stock(stock_ticker))

        super().__init__(stocks)
