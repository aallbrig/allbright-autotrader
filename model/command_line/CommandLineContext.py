from model.command_line.CommandLinePrinter import CommandLinePrinter


class CommandLineContext:
    argv: list[str] = []
    command_line: CommandLinePrinter = None

    def __init__(self, command_line: CommandLinePrinter, argv: list[str]):
        self.command_line = command_line
        self.argv = argv
