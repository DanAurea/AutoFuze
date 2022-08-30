from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetDaqListModeBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqListModeRequest(Cmd):
    PID = DataAcquisitionCommand.GET_DAQ_LIST_MODE
    
    _pack_   = 1
    _fields_ =  [
                    ('daq_list_number', c_uint16),
                ]

    def __init__(self, daq_list_number = 0xFF):
        self.daq_list_number = daq_list_number

class GetDaqListModeResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('reserved', c_uint16),
                    ('event_channel_number', c_uint16),
                    ('prescaler', c_uint8),
                    ('daq_list_number', c_uint8),
                ]

    def __init__(self, mode = GetDaqListModeBit(0xFF), event_channel_number = 0xFF, prescaler = 0xFF, daq_list_priority = 0xFF):
        self.mode                 = mode
        self.event_channel_number = event_channel_number
        self.prescaler            = prescaler
        self.daq_list_priority    = daq_list_priority