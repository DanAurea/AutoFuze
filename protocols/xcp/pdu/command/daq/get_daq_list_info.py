from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import DaqListPropertiesBit

class GetDaqListInfoRequest(object):
    
    def __init__(self):
        self._code            = DataAcquisitionCommand.GET_DAQ_LIST_INFO
        self._daq_list_number = 0xFF

class GetDaqListInfoResponse(object):
    
    def __init__(self):
        self._code                = StandardCommandCode.CONNECT
        self._daq_list_properties = DaqListPropertiesBit(0xFF)
        self._max_odt             = 0xFF
        self._max_odt_entires     = 0xFF
        self._fixed_event         = 0xFF