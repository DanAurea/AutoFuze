from ctypes import c_uint8

from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CommModeOptionalBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetCommModeInfo(Cmd):
    PID = StandardCommandCode.GET_COMM_MODE_INFO

class GetCommModeInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('reserved1', c_uint8),
                    ('comm_mode_optional', c_uint8),
                    ('reserved2', c_uint8),
                    ('max_bs', c_uint8),
                    ('min_st', c_uint8),
                    ('queue_size', c_uint8),
                    ('xcp_drive_version_number', c_uint8),
                ]

    def __init__(self, comm_mode_optional = CommModeOptionalBit(0xFF), max_bs = 0xFF, min_st = 0xFF, queue_size = 0xFF, xcp_drive_version_number = 0xFF):
        self.comm_mode_optional       = comm_mode_optional
        self.max_bs                   = max_bs
        self.min_st                   = min_st
        self.queue_size               = queue_size
        self.xcp_drive_version_number = xcp_drive_version_number