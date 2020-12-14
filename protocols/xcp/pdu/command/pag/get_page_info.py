from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PagePropertiesBit

class GetPageInfoRequest(object):
    
    def __init__(self):
        self._code           = PageSwitchingCommand.GET_PAGE_INFO
        self._segment_number = 0xFF
        self._page_number    = 0xFF

class GetPageInfoResponse(object):
    
    def __init__(self):
        self._code            = StandardCommandCode.CONNECT
        self._page_properties = PagePropertiesBit(0xFF)
        self._init_segment    = 0xFF