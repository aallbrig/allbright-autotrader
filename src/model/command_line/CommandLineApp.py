from typing import Optional

from src.model.command_line.CommandLinePrinter import CommandLinePrinter
from src.model.command_line.CommandLineCommand import CommandLineCommand
from src.model.command_line.CommandLineContext import CommandLineContext
from src.model.command_line.CommandRegistry import CommandRegistry


class CommandLineApp:
    _registry: CommandRegistry
    _command_line_printer: CommandLinePrinter
    _context: CommandLineContext

    def __init__(self, command_line_printer: CommandLinePrinter, registry: CommandRegistry):
        self._command_line_printer = command_line_printer
        self._registry = registry

    def run(self, argv: list[str]) -> int:
        maybe_command, command_argv = self._try_find_command(argv)
        # TODO: FEATURE_REQUEST: input validation for user input from the command console
        # for both valid_command and valid_command_argv
        valid_command = maybe_command
        valid_command_argv = command_argv
        if valid_command is not None:
            return valid_command.Execute(CommandLineContext(self._command_line_printer, valid_command_argv))
        else:
            return 1

    def _try_find_command(self, argv: list[str]) -> (Optional[CommandLineCommand], list[str]):
        # walk the argv string list until a valid command is found from the registry
        # FEATURE_REQUEST: support nested commands (e.g. main.py command nested-command --flag) (recursive?)
        maybe_command_string, argv_rest = (argv[0], argv[1:])
        maybe_command = self._registry.get(maybe_command_string)

        if maybe_command is not None:
            return maybe_command, argv_rest
        else:
            return None, None
