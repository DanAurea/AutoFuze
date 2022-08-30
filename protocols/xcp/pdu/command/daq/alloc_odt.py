from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class AllocOdtRequest(Cmd):
    PID = DataAcquisitionCommand.ALLOC_ODT
    
    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('daq_list_number', c_uint16),
                    ('odt_count', c_uint8),
                ]

    def __init__(self, daq_list_number = 0xFF, odt_count = 0xFF):
        self.daq_list_number = daq_list_number
        self.odt_count       = odt_count