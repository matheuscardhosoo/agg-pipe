"""Chain of responsabilities pattern"""
from src.agg_pipe.command_chain_descriptor import CommandChainDescriptor


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
