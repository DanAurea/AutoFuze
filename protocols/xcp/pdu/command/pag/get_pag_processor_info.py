from xcp.enum.command_code import PageSwitchingCommand
from ctypes import c_uint8

from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PagPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetPagProcessorInfoRequest(Cmd):
    PID = PageSwitchingCommand.GET_PAG_PROCESSOR_INFO
    
class GetPagProcessorInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_ = 1
    _fields_ =  [
                    ('max_segment', c_uint8),
                    ('pag_properties', c_uint8),
                ]

    def __init__(self, max_segment = 0xFF, pag_properties = PagPropertiesBit(0xFF)):
        self.max_segment    = max_segment
        self.pag_properties = pag_properties