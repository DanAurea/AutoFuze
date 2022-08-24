from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramVerifyRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_VERIFY

    def __init__(self):
        self._verification_mode  = 0xFF
        self._verification_type  = 0xFF
        self._verification_value = 0xFF