from src.model.command_line.CommandLine import CommandLine


class CommandLineContext:
    argv: list[str] = []
    command_line: CommandLine = None

    def __init__(self, command_line: CommandLine, argv: list[str]):
        self.command_line = command_line
        self.argv = argv
