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
    
    def __init__(self):
        self._mode = ConnectMode.NORMAL_MODE

class ConnectResponse(Res):
    """
    This class describes a connect request.
    """
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._ressource                   = RessourceBit(0xFF)
        self._comm_mode_basic             = CommModeBasicBit(0xFF)
        self._max_cto                     = 0xFF
        self._max_dto                     = 0xFFFF
        self._xcp_protocol_layer_version  = 0xFF
        self._xcp_transport_layer_version = 0xFF