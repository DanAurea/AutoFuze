from ctypes import c_uint8, c_uint16, c_uint32

from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramVerifyRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_VERIFY

    _pack_ = 1
    _fields_ =  [
                    ('verification_mode', c_uint8),
                    ('verification_type', c_uint16),
                    ('verification_value', c_uint32),
                ]

    def __init__(self, verification_mode = 0xFF, verification_type = 0xFF, verification_value = 0xFF):
        self.verification_mode  = verification_mode
        self.verification_type  = verification_type
        self.verification_value = verification_value