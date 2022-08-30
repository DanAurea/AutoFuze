from ctypes import c_uint8, c_uint16, c_uint32

from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramClearRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_CLEAR
    
    _pack_ = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('reserved', c_uint16),
                    ('clear_range', c_uint32),
                ]

    def __init__(self, mode = 0xFF, clear_range = 0xFFFF):
        self.mode        = mode
        self.clear_range = clear_range