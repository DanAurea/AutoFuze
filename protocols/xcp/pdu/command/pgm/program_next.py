from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.error_code import ErrorCode

class ProgramNextRequest(object):

    def __init__(self):
        self._code                = NvmProgrammingCommand.PROGRAM_NEXT
        self._number_data_element = 0xFF
        self._alignment           = 0xFF
        self._data_element        = bytearray()

class ProgramNextResponse(object):

    def __init__(self):
        self._code                         = StandardCommandCode.DISCONNECT
        self._err                          = ErrorCode.ERR_SEQUENCE
        self._number_expected_data_element = 0xFF
