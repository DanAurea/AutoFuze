from xcp.enum.command_code import NvmProgrammingCommandCode
from xcp.pdu.cto.cmd import Cmd

class ProgramReset(Cmd):
    PID = NvmProgrammingCommandCode.PROGRAM_RESET