from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSectorInfoRequest(Cmd):
    PID = NvmProgrammingCommand.GET_SECTOR_INFO

    def __init__(self):
        self._mode          = 0xFF
        self._sector_number = 0xFF

class GetSectorInfoResponse(Res):
    PID = StandardCommandCode.CONNECT

    def __init__(self):
        self._clear_sequence_number   = 0xFF
        self._program_sequence_number = 0xFF
        self._programming_method      = 0xFF
        self._sector_info             = 0xFF