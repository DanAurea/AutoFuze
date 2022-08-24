from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramClearRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_CLEAR
    
    def __init__(self):
        self._mode        = 0xFF
        self._clear_range = 0xFFFF