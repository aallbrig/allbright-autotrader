class CommandLineContext:
    argv: list[str] = []

    def __init__(self, argv: list[str]):
        self.argv = argv
