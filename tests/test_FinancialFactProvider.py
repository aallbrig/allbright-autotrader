import unittest

from model.FinancialFactProvider import FinancialFactProvider
from model.Stock import Stock
from model.StockInfoReport import StockInfoReport
from tests.test_fixtures.SpyStockInformationProvider import SpyStockInformationProvider


class FinancialFactProviderTests(unittest.TestCase):
    def test_financial_fact_provider_can_provide_facts_about_a_stock(self):
        stock_picks = [StockInfoReport(stock) for stock in [Stock(stock_pick) for stock_pick in ["TSLA"]]]
        sut = FinancialFactProvider(SpyStockInformationProvider(stock_info_reports=stock_picks))

        results = sut.inform_about_stocks()

        self.assertIsNot(None, results)

    def test_financial_fact_provider_can_provide_useful_facts_about_a_stock(self):
        stock_picks = [StockInfoReport(stock) for stock in [Stock(stock_pick) for stock_pick in ["TSLA"]]]
        sut = FinancialFactProvider(SpyStockInformationProvider(stock_info_reports=stock_picks))

        results = sut.inform_about_stocks()

        for result in results:
            self.assertTrue(issubclass(result.__class__, StockInfoReport))


if __name__ == '__main__':
    unittest.main()
