from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import SetCalPageBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetCalPageRequest(Cmd):
    PID = PageSwitchingCommand.GET_CAL_PAGE
    
    def __init__(self):
        self._mode                        =  SetCalPageBit(0xFF)
        self._logical_data_segment_number = 0xFF

class GetCalPageResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._logical_data_page_number = 0xFF