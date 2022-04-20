import os
import sys
from typing import Optional

from src.model.command_line.CommandLineCommand import CommandLineCommand
from src.model.command_line.CommandLineContext import CommandLineContext
from src.model.command_line.CommandRegistry import CommandRegistry


class CommandLineApp:
    _registry: CommandRegistry
    _context: CommandLineContext

    def __init__(self, registry: CommandRegistry):
        self._registry = registry

    def run(self, argv: list[str]) -> int:
        # FEATURE_REQUEST: input validation
        maybe_command, command_argv = self._try_find_command(argv)
        # FEATURE_REQUEST: validate command
        if maybe_command is not None:
            return maybe_command.Execute(CommandLineContext(command_argv))
        else:
            return os.EX_NOTFOUND

    def _try_find_command(self, argv: list[str]) -> (Optional[CommandLineCommand], list[str]):
        # walk the argv string list until a valid command is found from the registry
        # FEATURE_REQUEST: recursive?
        maybe_command_string, argv_rest = (argv[0], argv[1:])
        maybe_command = self._registry.get(maybe_command_string)

        if maybe_command is not None:
            return maybe_command, argv_rest
        else:
            return None, None
