from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.parameter_bit import SetDaqListModeBit
from xcp.pdu.cto.cmd import Cmd

class SetDaqListModeRequest(Cmd):
    PID = DataAcquisitionCommand.SET_DAQ_LIST_MODE
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('daq_list_number', c_uint16),
                    ('event_channel_number', c_uint16),
                    ('transmission_rate_prescaler', c_uint8),
                    ('daq_list_number', c_uint8),
                ]

    def __init__(self, mode = SetDaqListModeBit(0xFF), daq_list_number = 0xFF, event_channel_number = 0xFF, transmission_rate_prescaler = 0xFF, daq_list_priority = 0xFF):
        self.mode                        = mode
        self.daq_list_number             = daq_list_number
        self.event_channel_number        = event_channel_number
        self.transmission_rate_prescaler = transmission_rate_prescaler
        self.daq_list_priority           = daq_list_priority