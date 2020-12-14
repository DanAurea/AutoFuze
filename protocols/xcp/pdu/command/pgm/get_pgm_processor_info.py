from xcp.enum.command_code import NvmProgrammingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PgmPropertiesBit

class GetPgmProcessorInfoRequest(object):
    
    def __init__(self):
        self._code = NvmProgrammingCommand.GET_PGM_PROCESSOR_INFO

class GetPgmProcessorInfoResponse(object):
    
    def __init__(self):
        self._code           = StandardCommandCode.CONNECT
        self._pgm_properties = PgmPropertiesBit(0xFF)
        self._max_sector     = 0xFF