from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PagPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetPagProcessorInfoRequest(Cmd):
    PID = PageSwitchingCommand.GET_PAG_PROCESSOR_INFO
    
class GetPagProcessorInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._max_segment    = 0xFF
        self._pag_properties = PagPropertiesBit(0xFF)