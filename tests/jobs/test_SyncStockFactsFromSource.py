import unittest

from tests._test_fixtures.TestCommandLine import TestCommandLine
from src.jobs.SyncStockFactsFromSource import SyncStockFactsFromSource
from src.model.Stock import Stock
from src.model.StockInfoReport import StockInfoReport
from src.model.command_line.CommandLineContext import CommandLineContext
from tests._test_fixtures.ThirdPartyStockInfoProvider import TestThirdPartyStockInfoProvider


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
        message = ''
        expected_output_message = 'Stock: TSLA'
        test_input_reports = [StockInfoReport(Stock('TSLA'))]
        test_fact_provider = TestThirdPartyStockInfoProvider(stock_info_reports=test_input_reports)
        test_command_line = TestCommandLine(self._set_intercepted_message)
        test_argv = []
        test_context = CommandLineContext(test_command_line, test_argv)
        sut = SyncStockFactsFromSource(test_fact_provider)

        sut.Execute(test_context)
        self.assertEqual(expected_output_message, self._get_intercepted_message())


if __name__ == '__main__':
    unittest.main()
