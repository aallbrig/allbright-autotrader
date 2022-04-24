from typing import Callable, Optional

from model.command_line.CommandLineCommand import CommandLineCommand


class CommandRegistry:
    """CommandRegistry
        This class is used to bundled up commands used for a CLI
    """
    _registry_lookup: dict[str, Callable[[], CommandLineCommand]] = {}

    @staticmethod
    def validate_command_producing_function(command_producing_function: Callable[[], CommandLineCommand]) -> bool:
        command = command_producing_function()
        return CommandRegistry.validate_command(command)

    @staticmethod
    def validate_command(command: CommandLineCommand) -> bool:
        return issubclass(command.__class__, CommandLineCommand)

    def can_get(self, command_string: str) -> bool:
        return command_string in self._registry_lookup.keys()

    def get(self, command_string: str) -> Optional[CommandLineCommand]:
        if self.can_get(command_string):
            lazy_callable = self._registry_lookup[command_string]
            command = lazy_callable()
            return command if CommandRegistry.validate_command(command) else None
        else:
            # TODO: think more about what happens when registry doesn't produce a (valid) command
            # I'm kinda thinking about an exception system designed for this
            # maybe something like LookupException or some sort of Status object?
            # Definitely think through this design more
            return None

    def set(self, command_string: str, command_producing_function: Callable[[], CommandLineCommand]):
        self._registry_lookup[command_string] = command_producing_function
