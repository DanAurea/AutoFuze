from ctypes import c_uint8, c_uint32

from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd

class ShortUpload(Cmd):
    PID = StandardCommandCode.SHORT_UPLOAD
    
    _pack_   = 1
    _fields_ =  [
                    ('number_of_data_element', c_uint8),
                    ('reserved', c_uint8),
                    ('address_extension', c_uint8),
                    ('address', c_uint32),
                ]

    def __init__(self, number_of_data_element = 0xFF, address_extension = 0xFF, address = 0xFF):
        self.number_of_data_element = number_of_data_element
        self.address_extension      = address_extension
        self.address                = address