from ctypes import c_uint8

from xcp.enum.command_code import PageSwitchCommandCode
from xcp.enum.parameter_bit import SetCalPageBit
from xcp.pdu.cto.cmd import Cmd

class SetCalPage(Cmd):
    PID = PageSwitchCommandCode.SET_CAL_PAGE
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('logical_data_segment_number', c_uint8),
                    ('logical_data_page_number', c_uint8),
                ]

    def __init__(self, mode = SetCalPageBit(0xFF), logical_data_segment_number = 0xFF, logical_data_page_number = 0xFF):
        self.mode                        = mode
        self.logical_data_segment_number = logical_data_segment_number
        self.logical_data_page_number    = logical_data_page_number