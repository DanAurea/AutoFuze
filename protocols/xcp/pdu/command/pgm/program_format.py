from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramFormatRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_FORMAT

    def __init__(self):
        self._compression_method = 0xFF
        self._encryption_method  = 0xFF
        self._programming_method = 0xFF
        self._access_method      = 0xFF