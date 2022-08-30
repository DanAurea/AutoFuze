from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import TimestamModeBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqResolutionInfoRequest(Cmd):
    PID = DataAcquisitionCommand.DAQ_RESOLUTION_INFO

class GetDaqResolutionInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_ = 1
    _fields_ =  [
                    ('granularity_odt_entry_size_daq', c_uint8),
                    ('max_odt_entry_size_daq', c_uint8),
                    ('granularity_odt_entry_size_stim', c_uint8),
                    ('max_odt_entry_size_stim', c_uint8),
                    ('timestamp_mode', c_uint8),
                    ('timestamp_ticks', c_uint16),
                ]

    def __init__(self, granularity_odt_entry_size_daq = 0xFF, max_odt_entry_size_daq = 0xFF, granularity_odt_entry_size_stim = 0xFF, max_odt_entry_size_stim = 0xFF, timestamp_mode = TimestamModeBit(0xFF), timestamp_ticks = 0xFF):
        self.granularity_odt_entry_size_daq  = granularity_odt_entry_size_daq
        self.max_odt_entry_size_daq          = max_odt_entry_size_daq
        self.granularity_odt_entry_size_stim = granularity_odt_entry_size_stim
        self.max_odt_entry_size_stim         = max_odt_entry_size_stim
        self.timestamp_mode                  = timestamp_mode
        self.timestamp_ticks                 = timestamp_ticks