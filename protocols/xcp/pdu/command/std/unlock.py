from ctypes import c_uint8

from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CurrentSessionStatusBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class UnlockRequest(Cmd):
    PID = StandardCommandCode.UNLOCK
    
    def __init__(self, length = 0xFF, key = b''):
        self.length = length
        self.key    = key

    def __bytes__(self):
        class Payload(Cmd):
            PID = UnlockRequest.PID
            
            _pack_   = 1
            _fields_ =  [
                            ('length', c_uint8),
                            ('key', self.length * c_uint8),
                        ]

        payload = Payload()
        payload.length = self.length
        payload.key    = (self.length * c_uint8)(*self.key)

        return bytes(payload)

class UnlockResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('resource_protection_status', c_uint8)
                ]

    def __init__(self, resource_protection_status = CurrentSessionStatusBit(0xFF)):
        self.resource_protection_status = CurrentSessionStatusBit(0xFF)