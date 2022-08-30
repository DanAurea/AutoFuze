from ctypes import c_uint8

from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetSegmentModeBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSegmentModeRequest(Cmd):
    PID = PageSwitchingCommand.GET_SEGMENT_MODE

    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('segment_number', c_uint8),
                ]

    def __init__(self, segment_number = 0xFF):
        self.segment_number = segment_number

class GetSegmentModeResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('mode', c_uint8),
                ]

    def __init__(self, mode = GetSegmentModeBit(0xFF)  ):
        self.mode = mode