from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PagePropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetPageInfoRequest(Cmd):
    PID = PageSwitchingCommand.GET_PAGE_INFO
    
    def __init__(self):
        self._segment_number = 0xFF
        self._page_number    = 0xFF

class GetPageInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._page_properties = PagePropertiesBit(0xFF)
        self._init_segment    = 0xFF