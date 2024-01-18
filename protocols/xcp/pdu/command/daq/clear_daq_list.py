from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.pdu.cto.cmd import Cmd

class ClearDaqList(Cmd):
    PID = DataAcquisitionCommandCode.CLEAR_DAQ_LIST
        
    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('daq_list_number', c_uint16),
                ]

    def __init__(self, daq_list_number = 0xFF):
        self.daq_list_number = daq_list_number