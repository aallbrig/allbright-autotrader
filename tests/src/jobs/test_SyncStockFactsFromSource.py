import unittest

from tests.test_fixtures.TestCommandLinePrinter import TestCommandLinePrinter
from src.jobs.SyncStockFactsFromSource import SyncStockFactsFromSource
from model.Stock import Stock
from model.StockInfoReport import StockInfoReport
from model.command_line.CommandLineContext import CommandLineContext
from tests.test_fixtures.ThirdPartyStockInfoProvider import TestThirdPartyStockInfoProvider


class TestSyncStockFactsFromSource(unittest.TestCase):
    # TODO: how can I do what I want to do here
    #  without maintaining state in the class?
    # TODO: delete
    _intercepted_message: str

    # TODO: delete
    def _get_intercepted_message(self):
        return self._intercepted_message

    # TODO: delete
    def _set_intercepted_message(self, message: str):
        self._intercepted_message = message

    def test_message_output_when_TSLA_passed_in(self):
        expected_output_message = 'Stock: TSLA'
        test_input_reports = [StockInfoReport(Stock('TSLA'))]
        test_fact_provider = TestThirdPartyStockInfoProvider(stock_info_reports=test_input_reports)
        test_command_line = TestCommandLinePrinter(self._set_intercepted_message)
        test_argv = []
        test_context = CommandLineContext(test_command_line, test_argv)
        sut = SyncStockFactsFromSource(test_fact_provider)

        sut.Execute(test_context)
        self.assertEqual(expected_output_message, self._get_intercepted_message())


if __name__ == '__main__':
    unittest.main()