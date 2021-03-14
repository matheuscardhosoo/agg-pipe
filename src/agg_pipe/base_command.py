"""Abstraction of a command execution"""
from pandas import DataFrame


class BaseCommand():
    """
    Base class to abstract a command execution.
    """

    def __init__(self, id, command, condition_to_execute, condition_to_proceed):
        pass

    def execute(self, input: DataFrame) -> DataFrame:
        pass

    def where_to_go(self, data_frame_to_analyze: DataFrame) -> str:
        pass
