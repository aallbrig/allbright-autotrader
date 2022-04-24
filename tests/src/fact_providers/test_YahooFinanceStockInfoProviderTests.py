import unittest

from model.Stock import Stock
from src.fact_providers.YahooFinanceStockInfoProvider import YahooFinanceStockInfoProvider


class YahooFinanceStockInfoProviderTests(unittest.TestCase):
    def test_provider_provides_yahoo_data(self):
        test_stocks = [Stock("TSLA")]
        sut = YahooFinanceStockInfoProvider(test_stocks)
        sut.retrieve_now_summary()

        self.assertTrue(test_stocks[0].now_summary() is not None)


if __name__ == '__main__':
    unittest.main()
