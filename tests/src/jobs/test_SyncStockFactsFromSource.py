import unittest

from src.fact_providers.YahooFinanceStockInfoProvider import YahooFinanceStockInfoProvider
from tests.test_fixtures.MessageInterceptor import MessageInterceptor
from tests.test_fixtures.SpyCommandLinePrinter import SpyCommandLinePrinter
from src.jobs.SyncStockFactsFromSource import SyncStockFactsFromSource
from model.Stock import Stock
from model.command_line.CommandLineContext import CommandLineContext
from tests.test_fixtures.SpyStockFromFileProvider import SpyStockFromFileProvider
from tests.test_fixtures.SpyStockInformationProvider import SpyStockInformationProvider


class TestSyncStockFactsFromSource(unittest.TestCase):

    def test_message_output_when_TSLA_passed_in(self):
        expected_output_message = 'Stock: TSLA Current Price: 0.0'
        test_fact_provider = SpyStockInformationProvider(stocks=[Stock('TSLA')])
        sut = SyncStockFactsFromSource(test_fact_provider, SpyStockFromFileProvider(
            on_get_stocks=lambda: [Stock('TSLA')],
            on_is_valid=lambda: True
        ))
        message_interceptor = MessageInterceptor()
        test_command_line = SpyCommandLinePrinter(message_interceptor.set_intercepted_message)
        test_argv = []
        test_context = CommandLineContext(test_command_line, test_argv)

        sut.Execute(test_context)

        self.assertEqual(expected_output_message, message_interceptor.get_intercepted_message())

    def test_getting_stocks_picks_from_file(self):
        expected_output_message = 'Stock: TSLA Current Price: 0.0'
        sut = SyncStockFactsFromSource(YahooFinanceStockInfoProvider(), SpyStockFromFileProvider(
            lambda: [Stock('TSLA')],
            lambda: True
        ))
        message_interceptor = MessageInterceptor()
        test_command_line = SpyCommandLinePrinter(message_interceptor.set_intercepted_message)
        test_argv = []
        test_context = CommandLineContext(test_command_line, test_argv)

        sut.Execute(test_context)

        self.assertEqual(expected_output_message, message_interceptor.get_intercepted_message())


if __name__ == '__main__':
    unittest.main()
