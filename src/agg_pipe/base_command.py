"""Abstraction of a command execution"""
from typing import Optional

from pandas import DataFrame


class BaseCommand():
    """
    Base class to abstract a command execution.
    """

    def __init__(self, unique_key, command, condition_to_execute, condition_to_proceed):
        self._unique_key = unique_key
        self._command = command
        self._condition_to_execute = condition_to_execute
        self._condition_to_proceed = condition_to_proceed

    def execute(self, data_frame_to_process: DataFrame) -> Optional[DataFrame]:
        """
        Execute the command for the given DataFrame.
        """

    def where_to_go(self, data_frame_to_analyze: DataFrame) -> Optional[str]:
        """
        Defines the unique_key of the next Command based on the given DataFrame.
        """
