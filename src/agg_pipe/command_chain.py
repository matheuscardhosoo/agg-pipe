"""Chain of responsabilities pattern"""
from agg_pipe.base_command import BaseCommand
from agg_pipe.command_chain_descriptor import CommandChainDescriptor
from agg_pipe.command_descriptor import CommandDescriptor


class CommandChain():
    """
    Iterator to scroll through a chain of commands (building and executing commands).
    """

    def __init__(self, command_chain_descriptor: CommandChainDescriptor):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __len__(self):
        pass

    def build(self, command_descriptor: CommandDescriptor) -> BaseCommand:
        """
        Build a BaseCommand class based on a CommandDescriptor.
        """
