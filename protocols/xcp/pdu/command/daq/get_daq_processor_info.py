from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.enum.parameter_bit import DaqKeyBit, DaqEventPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqProcessorInfo(Cmd):
    PID = DataAcquisitionCommandCode.GET_DAQ_PROCESSOR_INFO

class GetDaqProcessorInfoResponse(Res):
    PID = DataAcquisitionCommandCode.GET_DAQ_PROCESSOR_INFO

    _pack_   = 1
    _fields_ =  [
                    ('daq_properties', c_uint8),
                    ('max_daq', c_uint16),
                    ('max_event_channel', c_uint16),
                    ('min_daq', c_uint8),
                    ('daq_key_byte', c_uint8),
                ]

    def __init__(self, daq_properties = DaqEventPropertiesBit(0xFF), max_daq = 0xFF, max_event_channel = 0xFF, min_daq = 0xFF, daq_key_byte = DaqKeyBit(0xFF)):
        self.daq_properties    = daq_properties
        self.max_daq           = max_daq
        self.max_event_channel = max_event_channel
        self.min_daq           = min_daq
        self.daq_key_byte      = daq_key_byte