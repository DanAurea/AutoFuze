from ctypes import c_uint8

from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd

class TransportLayerCmdRequest(Cmd):
    """
    This class describes a connect request.
    """
    PID = StandardCommandCode.TRANSPORT_LAYER_CMD
        
    def __init__(self, sub_command_code = 0xFF, parameters = b''):
        self.sub_command_code = sub_command_code
        self.parameters       = parameters

    def __bytes__(self):
        class Payload(Cmd):
                _pack_   = 1
                _fields_ =  [
                                ('sub_command_code', c_uint8),
                                ('parameters', len(self.parameters) * c_uint8),
                            ]

        payload = Payload()
        payload.sub_command_code = self.sub_command_code
        payload.parameters = (len(self.parameters) * c_uint8)(*self.parameters)

        return bytes(payload)