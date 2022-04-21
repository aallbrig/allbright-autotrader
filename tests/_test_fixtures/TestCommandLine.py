from typing import Callable

from src.model.command_line.CommandLine import CommandLine


class TestCommandLine(CommandLine):
    _on_print: Callable[[str], None]

    def __init__(self, on_print: Callable[[str], None]):
        self._on_print = on_print

    def print(self, message: str):
        self._on_print(message)
