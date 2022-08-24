from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CommModePgmBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class ProgramStartRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_START

class ProgramStartResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._comm_mode_pgm  = CommModePgmBit(0xFF)
        self._max_cto_pgm    = 0xFF
        self._max_bs_pgm     = 0xFF
        self._min_st_pgm     = 0xFF
        self._queue_size_pgm = 0xFF