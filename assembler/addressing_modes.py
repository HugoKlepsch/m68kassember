from enum import Enum


class RegisterDirect:
    pass


class DataRegisterDirect(RegisterDirect):
    pass


class AddressRegisterDirect(RegisterDirect):
    pass


class AbsoluteData:
    pass


class AbsoluteShortData(AbsoluteData):
    pass


class AbsoluteLongData(AbsoluteData):
    pass


class RegisterIndirect:
    pass


class PostIncrementRegisterIndirect(RegisterIndirect):
    pass


class PreDecrementRegisterIndirect(RegisterIndirect):
    pass


class RegisterIndirectWithOffset(RegisterIndirect):
    pass


class RegisterIndirectWithOffsetAndIndex(RegisterIndirect):
    pass


class PCRelativeWithOffset(RegisterIndirect):
    pass


class PCRelativeWithOffsetAndIndex(RegisterIndirect):
    pass


class Immediate:
    pass


class QuickImmediate:
    pass


class ImpliedRegister:
    pass


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
