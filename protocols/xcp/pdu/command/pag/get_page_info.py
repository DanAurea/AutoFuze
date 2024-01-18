from ctypes import c_uint8

from xcp.enum.command_code import PageSwitchCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PagPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetPageInfo(Cmd):
    PID = PageSwitchCommandCode.GET_PAGE_INFO
            
    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('segment_number', c_uint8),
                    ('page_number', c_uint8),
                ]

    def __init__(self, segment_number = 0xFF, page_number = 0xFF):
        self.segment_number = segment_number
        self.page_number    = page_number

class GetPageInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('page_properties', c_uint8),
                    ('init_segment', c_uint8),
                ]

    def __init__(self, page_properties = PagPropertiesBit(0xFF), init_segment = 0xFF):
        self.page_properties = page_properties
        self.init_segment    = init_segment