from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PagePropertiesBit

class GetPageInfoResponse(object):
    
    def __init__(self):
        self._code            = StandardCommandCode.CONNECT
        self._page_properties = PagePropertiesBit(0xFF)
        self._init_segment    = 0xFF