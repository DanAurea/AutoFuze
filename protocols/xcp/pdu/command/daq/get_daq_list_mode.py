from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetDaqListModeBit

class GetDaqListModeRequest(object):
    
    def __init__(self):
        self._code            = DataAcquisitionCommand.GET_DAQ_LIST_MODE
        self._daq_list_number = 0xFF

class GetDaqListModeResponse(object):
    
    def __init__(self):
        self._code                 = StandardCommandCode.CONNECT
        self._mode                 = GetDaqListModeBit(0xFF)
        self._event_channel_number = 0xFF
        self._prescaler            = 0xFF
        self._daq_list_number      = 0xFF