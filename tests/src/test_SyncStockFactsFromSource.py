import unittest

from src.jobs.SimulateHistoricTrading import SimulateHistoricTrading


class SimulateHistoricTradingTests(unittest.TestCase):
    def historic_trading_can_be_simulated_on_input_stock(self):
    # TODO: add test back into project
    # def test_historic_trading_can_be_simulated_on_input_stock(self):
        sut = SimulateHistoricTrading()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
