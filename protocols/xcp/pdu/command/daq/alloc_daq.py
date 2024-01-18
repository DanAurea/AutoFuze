from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.pdu.cto.cmd import Cmd

class AllocDaq(Cmd):
    PID = DataAcquisitionCommandCode.ALLOC_DAQ
    
    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('daq_count', c_uint16),
                ]

    def __init__(self, daq_count = 0xFF):
        self.daq_count = daq_count