from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode

class GetSectorInfoRequest(object):

    def __init__(self):
        self._code          = NvmProgrammingCommand.GET_SECTOR_INFO
        self._mode          = 0xFF
        self._sector_number = 0xFF

class GetSectorInfoResponse(object):

    def __init__(self):
        self._code                    = StandardCommandCode.CONNECT
        self._clear_sequence_number   = 0xFF
        self._program_sequence_number = 0xFF
        self._programming_method      = 0xFF
        self._sector_info             = 0xFF