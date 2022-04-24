import unittest

from tests.test_fixtures.SpyCommandLinePrinter import SpyCommandLinePrinter
from main import build_command_registry
from model.command_line.CommandLineApp import CommandLineApp


class AcceptanceTests(unittest.TestCase):
    def test_command_line_tool_can_generate_stock_report(self):
        sut = CommandLineApp(SpyCommandLinePrinter(lambda: None), build_command_registry())
        expected_exit_code = 0

        exit_code = sut.run(['job-sync-facts'])

        self.assertEqual(expected_exit_code, exit_code)

    def test_command_line_tool_exits_with_appropriate_status_when_command_not_found(self):
        sut = CommandLineApp(SpyCommandLinePrinter(lambda: None), build_command_registry())
        expected_exit_code = 1

        exit_code = sut.run(['not-found-command'])

        self.assertEqual(expected_exit_code, exit_code)


if __name__ == '__main__':
    unittest.main()
