from ctypes import c_uint8, c_uint32

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class ReadDaq(Cmd):
    PID = DataAcquisitionCommandCode.READ_DAQ

class ReadDaqResponse(Res):
    PID = StandardCommandCode.CONNECT

    _pack_   = 1
    _fields_ =  [
                    ('bit_offset', c_uint8),
                    ('size_of_daq_element', c_uint8),
                    ('address_extension', c_uint8),
                    ('address', c_uint32),
                ]

    def __init__(self, bit_offset = 0xFF, size_of_daq_element = 0xFF, address_extension = 0xFF, address = 0xFF):
        self.bit_offset          = bit_offset
        self.size_of_daq_element = size_of_daq_element
        self.address_extension   = address_extension
        self.address             = address