from models.command_line.CommandLineContext import CommandLineContext


class CommandLineCommand:
    def Execute(self, context: CommandLineContext):
        raise NotImplementedError("Please Implement this method")
