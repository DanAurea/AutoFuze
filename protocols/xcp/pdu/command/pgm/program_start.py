from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CommModePgmBit

class ProgramStartRequest(object):
    
    def __init__(self):
        self._code = NvmProgrammingCommand.PROGRAM_START

class ProgramStartResponse(object):
    
    def __init__(self):
        self._code           = StandardCommandCode.CONNECT
        self._comm_mode_pgm  = CommModePgmBit(0xFF)
        self._max_cto_pgm    = 0xFF
        self._max_bs_pgm     = 0xFF
        self._min_st_pgm     = 0xFF
        self._queue_size_pgm = 0xFF