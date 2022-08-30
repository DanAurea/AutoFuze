from ctypes import c_uint8

from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import SetCalPageBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetCalPageRequest(Cmd):
    PID = PageSwitchingCommand.GET_CAL_PAGE
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('logical_data_segment_number', c_uint8),
                ]

    def __init__(self, mode = SetCalPageBit(0xFF), logical_data_segment_number = 0xFF):
        self.mode                        =  mode
        self.logical_data_segment_number = logical_data_segment_number

class GetCalPageResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('reserved1', c_uint8),
                    ('reserved2', c_uint8),
                    ('logical_data_page_number', c_uint8),
                ]

    def __init__(self, logical_data_page_number = 0xFF):
        self.logical_data_page_number = logical_data_page_number