from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.parameter_bit import DaqEventPropertiesBit

class GetDaqEventInfoRequest(object):
    
    def __init__(self):
        self._code                 = DataAcquisitionCommand.GET_DAQ_EVENT_INFO
        self._event_channel_number = 0xFF

class GetDaqEventInfoResponse(object):
    
    def __init__(self):
        self._code                      = StandardCommandCode.CONNECT
        self._daq_event_properties      = DaqEventPropertiesBit(0xFF)
        self._max_daq_list              = 0xFF
        self._event_channel_name_length = 0xFF
        self._event_channel_time_cycle  = 0xFF
        self._event_channel_time_unit   = 0xFF
        self._event_channel_priority    = 0xFF