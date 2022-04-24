import unittest
from typing import Callable

from tests.test_fixtures.TestCommandLinePrinter import TestCommandLinePrinter
from model.command_line.CommandLineApp import CommandLineApp
from model.command_line.CommandLineCommand import CommandLineCommand
from model.command_line.CommandLineContext import CommandLineContext
from model.command_line.CommandRegistry import CommandRegistry


class TestCommandLineCommand(CommandLineCommand):
    _test_callback: Callable[[CommandLineContext], None]

    def __init__(self, test_callback: Callable[[CommandLineContext], None]):
        self._test_callback = test_callback

    def Execute(self, context: CommandLineContext):
        if self._test_callback is not None:
            self._test_callback(context)


class CommandCalledTracker:
    called = False
    context = None

    def call(self, context: CommandLineContext):
        self.called = True
        self.context = context


class TestCommandLineApp(unittest.TestCase):
    def test_command_line_app_is_configurable(self):
        call_tracker = CommandCalledTracker()
        test_registry = CommandRegistry()
        test_registry.set("foo", lambda: TestCommandLineCommand(lambda cxt: call_tracker.call(cxt)))
        sut = CommandLineApp(TestCommandLinePrinter(lambda: None), test_registry)

        sut.run(["foo"])

        self.assertTrue(call_tracker.called)


if __name__ == '__main__':
    unittest.main()
