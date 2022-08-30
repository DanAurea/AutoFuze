from ctypes import c_uint8, c_uint16, c_uint32

from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd

class SetMtaRequest(Cmd):
    PID = StandardCommandCode.SET_MTA
    
    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint16),
                    ('address_extension', c_uint8),
                    ('address', c_uint32),
                ]

    def __init__(self, address_extension = 0xFF, address = 0xFF):
        self.address_extension = address_extension
        self.address           = address