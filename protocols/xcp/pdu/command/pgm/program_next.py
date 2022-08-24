from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.error_code import ErrorCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class ProgramNextRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_NEXT

    def __init__(self):
        self._number_data_element = 0xFF
        self._alignment           = 0xFF
        self._data_element        = bytearray()

class ProgramNextResponse(Res):

    def __init__(self):
        self._code                         = StandardCommandCode.DISCONNECT
        self._err                          = ErrorCode.ERR_SEQUENCE
        self._number_expected_data_element = 0xFF
