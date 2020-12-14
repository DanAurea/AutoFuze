from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import SetCalPageBit

class GetCalPageRequest(object):
    
    def __init__(self):
        self._code                        = PageSwitchingCommand.GET_CAL_PAGE
        self._mode                        =  SetCalPageBit(0xFF)
        self._logical_data_segment_number = 0xFF

class GetCalPageResponse(object):
    
    def __init__(self):
        self._code                     = StandardCommandCode.CONNECT
        self._logical_data_page_number = 0xFF