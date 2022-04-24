import unittest
from datetime import date
from datetime import timedelta

from src.model.Stock import Stock
from src.model.StockHistorian import StockHistorian


class TestStockHistorian(unittest.TestCase):
    def test_historian_can_get_3_days_of_stock_history(self):
        sut = StockHistorian(Stock('TSLA'))

        sut.discover_history(date.today(), date.today() - timedelta(days=3))


if __name__ == '__main__':
    unittest.main()
