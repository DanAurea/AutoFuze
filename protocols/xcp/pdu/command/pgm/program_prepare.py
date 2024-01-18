from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import NvmProgrammingCommandCode
from xcp.pdu.cto.cmd import Cmd

class ProgramPrepare(Cmd):
    PID = NvmProgrammingCommandCode.PROGRAM_PREPARE

    _pack_   = 1
    _fields_ =  [
                    ('not_used', c_uint8),
                    ('code_size', c_uint16),
                ]

    def __init__(self, code_size = 0xFF):
        self.code_size = code_size