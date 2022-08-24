from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.parameter_bit import SetCalPageBit
from xcp.pdu.cto.cmd import Cmd

class SetCalPageRequest(Cmd):
    PID = PageSwitchingCommand.SET_CAL_PAGE
    
    def __init__(self):
        self._mode                        = SetCalPageBit(0xFF)
        self._logical_data_segment_number = 0xFF
        self._logical_data_page_number    = 0xFF