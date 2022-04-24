import unittest

from tests.test_fixtures.TestCommandLinePrinter import TestCommandLinePrinter
from src.jobs.SyncStockFactsFromSource import SyncStockFactsFromSource
from src.model.Stock import Stock
from src.model.StockInfoReport import StockInfoReport
from src.model.command_line.CommandLineContext import CommandLineContext
from tests.test_fixtures.ThirdPartyStockInfoProvider import TestThirdPartyStockInfoProvider


class TestSimulateHistoricTrading(unittest.TestCase):
    def test_command_answer_to_one_question(self):
        # sut = SimulateHistoricTrading

        # sut.Execute(test_context)
        # self.assertEqual(expected_output_message, self._get_intercepted_message())
        pass


if __name__ == '__main__':
    unittest.main()
