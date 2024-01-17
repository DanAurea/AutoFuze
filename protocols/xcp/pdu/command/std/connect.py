from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import StandardCommandCode
from xcp.enum.connect_mode import ConnectMode
from xcp.enum.parameter_bit import RessourceBit, CommModeBasicBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class ConnectRequest(Cmd):
    """
    This class describes a connect request.
    """
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                ]

    def __init__(self, mode = ConnectMode.NORMAL):
        self.mode = mode

class ConnectResponse(Res):
    """
    This class describes a connect request.
    """
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('ressource', c_uint8),
                    ('comm_mode_basic', c_uint8),
                    ('max_cto', c_uint8),
                    ('max_dto', c_uint16),
                    ('xcp_protocol_layer_version', c_uint8),
                    ('xcp_transport_layer_version', c_uint8),
                ]

    def __init__(self, ressource = RessourceBit(0xFF), comm_mode_basic = CommModeBasicBit(0xFF), max_cto = 0xFF, max_dto = 0xFFFF, xcp_protocol_layer_version = 0xFF, xcp_transport_layer_version = 0xFF):
        self.ressource                   = ressource
        self.comm_mode_basic             = comm_mode_basic
        self.max_cto                     = max_cto
        self.max_dto                     = max_dto
        self.xcp_protocol_layer_version  = xcp_protocol_layer_version
        self.xcp_transport_layer_version = xcp_transport_layer_version