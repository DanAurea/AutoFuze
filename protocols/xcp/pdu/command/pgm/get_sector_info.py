from ctypes import c_uint8, c_uint32

from xcp.enum.command_code import NvmProgrammingCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSectorInfo(Cmd):
    PID = NvmProgrammingCommandCode.GET_SECTOR_INFO

    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('sector_number', c_uint8),
                ]

    def __init__(self, mode = 0xFF, sector_number = 0xFF):
        self.mode          = mode
        self.sector_number = sector_number

class GetSectorInfoResponse(Res):
    PID = StandardCommandCode.CONNECT

    _pack_   = 1
    _fields_ =  [
                    ('clear_sequence_number', c_uint8),
                    ('program_sequence_number', c_uint8),
                    ('programming_method', c_uint8),
                    ('sector_info', c_uint32),
                ]

    def __init__(self, clear_sequence_number = 0xFF, program_sequence_number = 0xFF, programming_method = 0xFF, sector_info = 0xFF):
        self.clear_sequence_number   = clear_sequence_number
        self.program_sequence_number = program_sequence_number
        self.programming_method      = programming_method
        self.sector_info             = sector_info