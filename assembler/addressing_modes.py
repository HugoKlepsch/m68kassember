from enum import Enum


class AddressingModeCategories(Enum):
    DATA = 0
    MEMORY = 1
    CONTROL = 2
    ALTERABLE = 3
    DATA_ALTERABLE = 4
    MEMORY_ALTERABLE = 5
    CONTROL_ALTERABLE = 6


class AddressingMode:
    categories = []


class RegisterDirect(AddressingMode):
    pass


class DataRegisterDirect(RegisterDirect):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
    ]


class AddressRegisterDirect(RegisterDirect):
    categories = [
        AddressingModeCategories.ALTERABLE,
    ]


class AbsoluteData(AddressingMode):
    pass


class AbsoluteShortData(AbsoluteData):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
        AddressingModeCategories.MEMORY_ALTERABLE,
        AddressingModeCategories.CONTROL_ALTERABLE,
    ]


class AbsoluteLongData(AbsoluteData):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
        AddressingModeCategories.MEMORY_ALTERABLE,
        AddressingModeCategories.CONTROL_ALTERABLE,
    ]


class RegisterIndirect(AddressingMode):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
        AddressingModeCategories.MEMORY_ALTERABLE,
        AddressingModeCategories.CONTROL_ALTERABLE,
    ]

class PostIncrementRegisterIndirect(RegisterIndirect):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
        AddressingModeCategories.MEMORY_ALTERABLE,
    ]


class PreDecrementRegisterIndirect(RegisterIndirect):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
        AddressingModeCategories.MEMORY_ALTERABLE,
    ]


class RegisterIndirectWithOffset(RegisterIndirect):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
        AddressingModeCategories.MEMORY_ALTERABLE,
        AddressingModeCategories.CONTROL_ALTERABLE,
    ]


class RegisterIndirectWithOffsetAndIndex(RegisterIndirect):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
        AddressingModeCategories.ALTERABLE,
        AddressingModeCategories.DATA_ALTERABLE,
        AddressingModeCategories.MEMORY_ALTERABLE,
        AddressingModeCategories.CONTROL_ALTERABLE,
    ]


class PCRelativeWithOffset(RegisterIndirect):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
    ]


class PCRelativeWithOffsetAndIndex(RegisterIndirect):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
    ]


class Immediate(AddressingMode):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
    ]


class QuickImmediate(AddressingMode):
    categories = [
        AddressingModeCategories.DATA,
        AddressingModeCategories.MEMORY,
        AddressingModeCategories.CONTROL,
    ]


class ImpliedRegister(AddressingMode):
    pass  # TODO understand this


class AddressingModes(Enum):
    DATA_REGISTER_DIRECT = DataRegisterDirect
    ADDRESS_REGISTER_DIRECT = AddressRegisterDirect
    ABS_SHORT_DATA = AbsoluteShortData
    ABS_LONG_DATA = AbsoluteLongData
    REGISTER_INDIRECT = RegisterIndirect
    POST_INC_REGISTER_INDIRECT = PostIncrementRegisterIndirect
    PRE_DEC_REGISTER_INDIRECT = PreDecrementRegisterIndirect
    REGISTER_INDIRECT_WITH_OFFSET = RegisterIndirectWithOffset
    REGISTER_INDIRECT_WITH_OFFSET_AND_INDEX = RegisterIndirectWithOffsetAndIndex
    PC_RELATIVE_WITH_OFFSET = PCRelativeWithOffset
    PC_RELATIVE_WITH_OFFSET_AND_INDEX = PCRelativeWithOffsetAndIndex
    IMMEDIATE = Immediate
    QUICK_IMMEDIATE = QuickImmediate
    IMPLIED_REGISTER = ImpliedRegister
