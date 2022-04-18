import unittest

from models.FinancialFactProvider import FinancialFactProvider
from models.Stock import Stock
from tests.utility.TestThirdPartyStockInfoProvider import TestThirdPartyStockInfoProvider


class FinancialFactProviderTests(unittest.TestCase):
    def test_financial_fact_provider_can_provide_facts_about_a_stock(self):
        stockpicks = ["TSLA"]
        sut = FinancialFactProvider([TestThirdPartyStockInfoProvider(stockpicks)])
        results = sut.inform_about_stocks()
        self.assertIsNot(None, results)

    def test_financial_fact_provider_can_provide_useful_facts_about_a_stock(self):
        stockpicks = ["TSLA"]
        sut = FinancialFactProvider([TestThirdPartyStockInfoProvider(stockpicks)])

        results = sut.inform_about_stocks()

        for result in results:
            self.assertTrue(issubclass(result, Stock))

    def test_financial_fact_provider_provide_facts_drawn_from_third_party_providers(self):
        stockpicks = ["TSLA"]
        sut = FinancialFactProvider([TestThirdPartyStockInfoProvider(stockpicks)])

        results = sut.inform_about_stocks()

        for result in results:
            self.assertTrue(issubclass(result, Stock))


if __name__ == '__main__':
    unittest.main()
