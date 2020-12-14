from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import TimestamModeBit

class GetDaqResolutionInfoRequest(object):
    
    def __init__(self):
        self._code = DataAcquisitionCommand.DAQ_RESOLUTION_INFO

class GetDaqResolutionInfoResponse(object):
    
    def __init__(self):
        self._code                            = StandardCommandCode.CONNECT
        self._granularity_odt_entry_size_daq  = 0xFF
        self._max_odt_entry_size_daq          = 0xFF
        self._granularity_odt_entry_size_stim = 0xFF
        self._max_odt_entry_size_stim         = 0xFF
        self._timestamp_mode                  = TimestamModeBit(0xFF)
        self._timestamp_ticks                 = 0xFF