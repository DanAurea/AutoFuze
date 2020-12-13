from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import DaqListPropertiesBit

class GetDaqListInfoResponse(object):
    
    def __init__(self):
        self._code                = StandardCommandCode.CONNECT
        self._daq_list_properties = DaqListPropertiesBit(0xFF)
        self._max_odt             = 0xFF
        self._max_odt_entires     = 0xFF
        self._fixed_event         = 0xFF