from xcp.enum.command_code import StandardCommandCode
from xcp.enum.connect_mode import ConnectMode
from xcp.enum.parameter_bit import RessourceBit, CommModeBasicBit

class ConnectRequest(object):
    """
    This class describes a connect request.
    """
    def __init__(self):
        self._code = StandardCommandCode.CONNECT
        self._mode = ConnectMode.NORMAL_MODE

class ConnectResponse(object):
    """
    This class describes a connect request.
    """
    def __init__(self):
        self._pid                         = StandardCommandCode.CONNECT
        self._ressource                   = RessourceBit(0xFF)
        self._comm_mode_basic             = CommModeBasicBit(0xFF)
        self._max_cto                     = 0xFF
        self._max_dto                     = 0xFFFF
        self._xcp_protocol_layer_version  = 0xFF
        self._xcp_transport_layer_version = 0xFF