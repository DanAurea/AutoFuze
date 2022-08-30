from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import SetRequestBit
from xcp.pdu.cto.cmd import Cmd

class SetRequest(Cmd):
    PID = StandardCommandCode.SET_REQUEST
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('session_configuration_id', c_uint16),
                ]

    def __init__(self, mode = SetRequestBit(0xFF), session_configuration_id = 0xFF):
        self.mode                     = mode
        self.session_configuration_id = session_configuration_id