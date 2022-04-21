import unittest

from src.model.FinancialFactProvider import FinancialFactProvider
from src.model import Stock
from src.model.StockInfoReport import StockInfoReport
from tests.utility.test_ThirdPartyStockInfoProvider import TestThirdPartyStockInfoProvider


class FinancialFactProviderTests(unittest.TestCase):
    def test_financial_fact_provider_can_provide_facts_about_a_stock(self):
        stock_picks = [StockInfoReport(stock) for stock in [Stock(stock_pick) for stock_pick in ["TSLA"]]]
        sut = FinancialFactProvider(TestThirdPartyStockInfoProvider(stock_picks))

        results = sut.inform_about_stocks()

        self.assertIsNot(None, results)

    def test_financial_fact_provider_can_provide_useful_facts_about_a_stock(self):
        stock_picks = [StockInfoReport(stock) for stock in [Stock(stock_pick) for stock_pick in ["TSLA"]]]
        sut = FinancialFactProvider(TestThirdPartyStockInfoProvider(stock_picks))

        results = sut.inform_about_stocks()

        for result in results:
            self.assertTrue(issubclass(result.__class__, StockInfoReport))


if __name__ == '__main__':
    unittest.main()
