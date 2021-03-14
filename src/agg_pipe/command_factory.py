"""Factory pattern"""
from src.agg_pipe.command_descriptor import CommandDescriptor
from src.agg_pipe.command.base_command import BaseCommand


class CommandFactory():
    """
    Factory to build command based on a command descriptor.
    """

    def __init__(self):
        pass

    def build(self, command_descriptor: CommandDescriptor) -> BaseCommand:
        pass
