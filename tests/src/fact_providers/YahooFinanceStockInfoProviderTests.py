import unittest

from models.Stock import Stock
from src.fact_providers.YahooFinanceStockInfoProvider import YahooFinanceStockInfoProvider


class YahooFinanceStockInfoProviderTests(unittest.TestCase):
    def test_provider_provides_yahoo_data(self):
        test_stocks = [Stock("TSLA")]
        sut = YahooFinanceStockInfoProvider(test_stocks)
        results = sut.retrieve_stock_info()

        self.assertIsNot(None, results)


if __name__ == '__main__':
    unittest.main()
