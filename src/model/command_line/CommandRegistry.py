from typing import Callable, Optional

from src.model.command_line.CommandLineCommand import CommandLineCommand


class CommandRegistry:
    """CommandRegistry
        this class is meant to encapsulate lazily loading command line commands
    """
    _registry_lookup: dict[str, Callable[[], CommandLineCommand]] = {}

    def get(self, command_string: str) -> Optional[CommandLineCommand]:
        if command_string in self._registry_lookup.keys():
            lazy_callable = self._registry_lookup[command_string]
            # Check that when lazy_callable is executed, the return type is CommandLineCommand?
            # aka validation logic?
            return lazy_callable()
        else:
            # TODO: think more about what happens when registry doesn't produce a (valid) command
            return None

    def set(self, command_string: str, command_producing_function: Callable[[], CommandLineCommand]):
        # FEATURE_REQUEST: input validation
        self._registry_lookup[command_string] = command_producing_function
