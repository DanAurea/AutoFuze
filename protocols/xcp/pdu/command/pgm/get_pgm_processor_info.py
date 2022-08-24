from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PgmPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetPgmProcessorInfoRequest(Cmd):
    PID = NvmProgrammingCommand.GET_PGM_PROCESSOR_INFO
    
class GetPgmProcessorInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._pgm_properties = PgmPropertiesBit(0xFF)
        self._max_sector     = 0xFF