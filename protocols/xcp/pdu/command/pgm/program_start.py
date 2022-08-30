from ctypes import c_uint8

from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CommModePgmBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class ProgramStartRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_START

class ProgramStartResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('comm_mode_pgm', c_uint8),
                    ('max_cto_pgm', c_uint8),
                    ('max_bs_pgm', c_uint8),
                    ('min_st_pgm', c_uint8),
                    ('queue_size_pgm', c_uint8),
                ]

    def __init__(self, comm_mode_pgm = CommModePgmBit(0xFF), max_cto_pgm = 0xFF, max_bs_pgm = 0xFF, min_st_pgm = 0xFF, queue_size_pgm = 0xFF):
        self.comm_mode_pgm  = comm_mode_pgm
        self.max_cto_pgm    = max_cto_pgm
        self.max_bs_pgm     = max_bs_pgm
        self.min_st_pgm     = min_st_pgm
        self.queue_size_pgm = queue_size_pgm