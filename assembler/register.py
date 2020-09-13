from enum import Enum
from typing import List


class RegisterType(Enum):
    DATA = 0
    ADDRESS = 1
    PC = 2
    STATUS = 3


class Register:
    def __init__(self, aliases: List[str], size: int, typ: RegisterType):
        """
        Describe a register
        :param aliases: Names this register can go by
        :param size: Size in bits
        :param typ: Register type
        """
        self.aliases = aliases
        self.size = size
        self.typ = typ


class Registers(Enum):
    D0 = Register(["D0"], 32, RegisterType.DATA)
    D1 = Register(["D1"], 32, RegisterType.DATA)
    D2 = Register(["D2"], 32, RegisterType.DATA)
    D3 = Register(["D3"], 32, RegisterType.DATA)
    D4 = Register(["D4"], 32, RegisterType.DATA)
    D5 = Register(["D5"], 32, RegisterType.DATA)
    D6 = Register(["D6"], 32, RegisterType.DATA)
    D7 = Register(["D7"], 32, RegisterType.DATA)

    A0 = Register(["A0"], 32, RegisterType.ADDRESS)
    A1 = Register(["A1"], 32, RegisterType.ADDRESS)
    A2 = Register(["A2"], 32, RegisterType.ADDRESS)
    A3 = Register(["A3"], 32, RegisterType.ADDRESS)
    A4 = Register(["A4"], 32, RegisterType.ADDRESS)
    A5 = Register(["A5"], 32, RegisterType.ADDRESS)
    A6 = Register(["A6"], 32, RegisterType.ADDRESS)
    A7 = Register(["A7", "SP", "USP", "SSP"], 32, RegisterType.ADDRESS)

    PC = Register(["PC"], 32, RegisterType.ADDRESS)

    SR = Register(["SR"], 16, RegisterType.STATUS)
    SB = Register(["SB"], 8, RegisterType.STATUS)
    CCR = Register(["CCR"], 8, RegisterType.STATUS)
