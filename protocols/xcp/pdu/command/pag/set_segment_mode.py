from xcp.enum.command_code import PageSwitchCommandCode
from xcp.enum.parameter_bit import SetSegmentModeBit
from xcp.pdu.cto.cmd import Cmd

from ctypes import c_uint8

class SetSegmentMode(Cmd):
    PID = PageSwitchCommandCode.SET_SEGMENT_MODE

    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('segment_number', c_uint8),
                ]

    def __init__(self, mode = SetSegmentModeBit(0xFF), segment_number = 0xFF):
        self.mode           = mode
        self.segment_number = segment_number