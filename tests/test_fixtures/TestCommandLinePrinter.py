from typing import Callable

from model.command_line.CommandLinePrinter import CommandLinePrinter


class TestCommandLinePrinter(CommandLinePrinter):
    _on_print: Callable[[str], None]

    def __init__(self, on_print: Callable[[str], None]):
        self._on_print = on_print

    def print(self, message: str):
        self._on_print(message)
