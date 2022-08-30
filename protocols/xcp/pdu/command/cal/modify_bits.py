from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class ModifyBitsRequest(Cmd):
    PID = CalibrationCommandCode.MODIFY_BITS
    
    _pack_  = 1
    _fields_ =  [
                    ('shift_value', c_uint8),
                    ('and_mask', c_uint16),
                    ('or_mask', c_uint16),
                ]

    def __init__(self, shift_value = 0xFF, and_mask = 0xFF, or_mask = 0xFF):
        self.shift_value = shift_value
        self.and_mask    = and_mask
        self.or_mask     = or_mask