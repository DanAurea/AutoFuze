from ctypes import c_uint8

from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSeed(Cmd):
    PID = StandardCommandCode.GET_SEED
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('resource', c_uint8),
                ]

    def __init__(self, mode = 0xFF, resource = 0xFF):
        self.mode     = mode
        self.resource = resource

class GetSeedResponse(Res):
    PID = StandardCommandCode.CONNECT

    def __init__(self, length = 0xFF, seed = b''):
        self.length = length
        self.seed   = seed

    def __bytes__(self):
        class Payload(Res):
            PID = GetSeedResponse.PID
            
            _pack_   = 1
            _fields_ =  [
                            ('length', c_uint8),
                            ('seed', self.length * c_uint8),
                        ]

        payload = Payload()
        payload.length = self.length
        payload.seed = (self.length * c_uint8)(*self.seed)

        return bytes(payload)