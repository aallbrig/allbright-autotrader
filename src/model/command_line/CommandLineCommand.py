from src.model.command_line.CommandLineContext import CommandLineContext


class CommandLineCommand:
    def Execute(self, context: CommandLineContext) -> int:
        raise NotImplementedError("Please Implement this method")
