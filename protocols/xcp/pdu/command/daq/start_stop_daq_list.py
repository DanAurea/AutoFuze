from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class StartStopDaqListRequest(Cmd):
    PID = DataAcquisitionCommand.START_STOP_DAQ_LIST
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('daq_list_number', c_uint16),
                ]

    def __init__(self, mode = 0xFF, daq_list_number = 0xFF):
        self.mode            = mode
        self.daq_list_number = daq_list_number

class StartStopDaqListResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('first_pid', c_uint8),
                ]

    def __init__(self, first_pid = 0xFF):
        self.first_pid = first_pid