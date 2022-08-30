from ctypes import c_uint8

from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramFormatRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_FORMAT

    _pack_   = 1
    _fields_ =  [
                    ('compression_method', c_uint8),
                    ('encryption_method', c_uint8),
                    ('programming_method', c_uint8),
                    ('access_method', c_uint8),
                ]

    def __init__(self, compression_method = 0xFF, encryption_method = 0xFF, programming_method = 0xFF, access_method = 0xFF):
        self.compression_method = compression_method
        self.encryption_method  = encryption_method
        self.programming_method = programming_method
        self.access_method      = access_method