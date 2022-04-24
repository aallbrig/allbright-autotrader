import unittest

from tempfile import NamedTemporaryFile
from tests.test_fixtures.SpyCommandLinePrinter import SpyCommandLinePrinter
from tests.test_fixtures.MessageInterceptor import MessageInterceptor
from main import build_command_registry
from model.command_line.CommandLineApp import CommandLineApp


class AcceptanceTests(unittest.TestCase):
    def test_command_line_tool_can_generate_stock_report_from_input_file(self):
        message_interceptor = MessageInterceptor()
        sut = CommandLineApp(SpyCommandLinePrinter(message_interceptor.set_intercepted_message),
                             build_command_registry())
        expected_message = "Stock: TSLA"
        test_input_file = NamedTemporaryFile()
        with open(test_input_file.name, 'w') as f:
            f.write("TSLA\n")

        sut.run(['job-sync-facts', '--input-file', test_input_file.name])
        test_input_file.close()

        self.assertEqual(expected_message, message_interceptor.get_intercepted_message())

    def test_command_line_tool_requires_input_file(self):
        sut = CommandLineApp(SpyCommandLinePrinter(lambda: None), build_command_registry())
        expected_exit_code = 1

        exit_code = sut.run(['job-sync-facts'])

        self.assertEqual(expected_exit_code, exit_code)

    def test_command_line_tool_exits_with_appropriate_status_when_command_not_found(self):
        sut = CommandLineApp(SpyCommandLinePrinter(lambda: None), build_command_registry())
        expected_exit_code = 1

        exit_code = sut.run(['not-found-command'])

        self.assertEqual(expected_exit_code, exit_code)


if __name__ == '__main__':
    unittest.main()
