from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import DaqEventPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqEventInfo(Cmd):
    PID = DataAcquisitionCommandCode.GET_DAQ_EVENT_INFO
    
    _pack_ = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('event_channel_number', c_uint16),
                ]

    def __init__(self, event_channel_number = 0xFF):
        self.event_channel_number = event_channel_number

class GetDaqEventInfoResponse(Res):
    PID = StandardCommandCode.CONNECT

    _pack_ = 1
    _fields_ =  [
                    ('daq_event_properties', c_uint8),
                    ('max_daq_list', c_uint8),
                    ('event_channel_name_length', c_uint8),
                    ('event_channel_time_cycle', c_uint8),
                    ('event_channel_time_unit', c_uint8),
                    ('event_channel_priority', c_uint8),
                ]
    
    def __init__(self, daq_event_properties = DaqEventPropertiesBit(0xFF), max_daq_list = 0xFF, event_channel_name_length = 0xFF, event_channel_time_cycle  = 0xFF, event_channel_time_unit = 0xFF, event_channel_priority = 0xFF):
        self.daq_event_properties      = daq_event_properties
        self.max_daq_list              = max_daq_list
        self.event_channel_name_length = event_channel_name_length
        self.event_channel_time_cycle  = event_channel_time_cycle
        self.event_channel_time_unit   = event_channel_time_unit
        self.event_channel_priority    = event_channel_priority