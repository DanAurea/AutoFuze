from ctypes import c_uint8, c_uint32

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqClock(Cmd):
    PID = DataAcquisitionCommandCode.GET_DAQ_CLOCK

class GetDaqClockResponse(Res):
    PID = StandardCommandCode.CONNECT
        
    _pack_   = 1
    _fields_ =  [
                    ('reserved', 3 * c_uint8),
                    ('receive_timestamp', c_uint32),
                ]

    def __init__(self, receive_timestamp = 0xFF):
        self.receive_timestamp = receive_timestamp