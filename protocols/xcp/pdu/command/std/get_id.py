from ctypes import c_uint8, c_uint16, c_uint32

from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetIdRequest(Cmd):
    PID = StandardCommandCode.GET_ID
    
    _pack_   = 1
    _fields_ =  [
                    ('requested_identification_type', c_uint8),
                ]

    def __init__(self, requested_identification_type = 0xFF):
        self.requested_identification_type = requested_identification_type

class GetIdResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self, mode = 0xFF, length = 0xFF, identification = b''):
        self.mode           = mode
        self.length         = length
        self.identification = identification

    def __bytes__(self):

        class Payload(Res):
            _pack_   = 1
            _fields_ =  [
                            ('mode', c_uint8),
                            ('reserved', c_uint16),
                            ('length', c_uint32),
                            ('identification', self.length * c_uint8),
                        ]

        payload = Payload()
        payload.mode           = self.mode
        payload.length         = self.length
        payload.identification = (c_uint8 * len(self.identification))(*self.identification)

        return bytes(payload)
