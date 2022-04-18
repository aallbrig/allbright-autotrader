import unittest

from src.jobs.SimulateHistoricTrading import SimulateHistoricTrading


class SimulateHistoricTradingTests(unittest.TestCase):
    def test_historic_trading_can_be_simulated_on_input_stock(self):
        sut = SimulateHistoricTrading()
        self.assertEqual(True, False)  # add assertion here

    def test_historic_trading_can_not_be_simulated_on_zero_input_stock(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
