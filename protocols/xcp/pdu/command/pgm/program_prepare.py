from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramPrepareRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_PREPARE

    def __init__(self):
        self._code_size = 0xFF