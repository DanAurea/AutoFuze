from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramResetRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_RESET