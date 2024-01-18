from ctypes import c_uint8

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.pdu.cto.cmd import Cmd

class StartStopSynch(Cmd):
    PID = DataAcquisitionCommandCode.START_STOP_SYNCH
    
    _pack_ = 1
    _fields_ = [
                    ('mode', c_uint8),
                ]

    def __init__(self, mode = 0xFF):
        self.mode = mode