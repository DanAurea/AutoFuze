from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PagPropertiesBit

class GetPagProcessorInfoResponse(object):
    
    def __init__(self):
        self._code           = StandardCommandCode.CONNECT
        self._max_segment    = 0xFF
        self._pag_properties = PagPropertiesBit(0xFF)