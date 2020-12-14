from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.parameter_bit import SetCalPageBit

class SetCalPageRequest(object):
    
    def __init__(self):
        self._code                        = PageSwitchingCommand.SET_CAL_PAGE
        self._mode                        = SetCalPageBit(0xFF)
        self._logical_data_segment_number = 0xFF
        self._logical_data_page_number    = 0xFF