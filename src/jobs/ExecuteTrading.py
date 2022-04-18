from models.command_line.CommandLineCommand import CommandLineCommand


class ExecuteTrading(CommandLineCommand):
    def Execute(self, context):
        # If facts offline cache not filled, hydrate that data
        # If historic data simulation has not been run, run it
        # Based on strategies (loaded up in code? loaded up from a directory that implement an abstract class?)
        pass
