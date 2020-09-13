from enum import Enum
from typing import List


class OperandSize:
    def __init__(self, size: int, aliases: List[str]):
        """
        Instruction size defintion
        :param size: Size in bits of the operand
        :param aliases: Symbol used to denote this size
        """
        self.size = size
        self.aliases = aliases


class OperandSizes(Enum):
    BYTE = OperandSize(8, ["B"])
    WORD = OperandSize(16, ["W"])
    LONG_WORD = OperandSize(32, ["L"])
