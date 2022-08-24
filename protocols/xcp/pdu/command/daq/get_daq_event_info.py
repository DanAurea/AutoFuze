from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.parameter_bit import DaqEventPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqEventInfoRequest(Cmd):
    PID = DataAcquisitionCommand.GET_DAQ_EVENT_INFO
    
    def __init__(self):
        self._event_channel_number = 0xFF

class GetDaqEventInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._daq_event_properties      = DaqEventPropertiesBit(0xFF)
        self._max_daq_list              = 0xFF
        self._event_channel_name_length = 0xFF
        self._event_channel_time_cycle  = 0xFF
        self._event_channel_time_unit   = 0xFF
        self._event_channel_priority    = 0xFF