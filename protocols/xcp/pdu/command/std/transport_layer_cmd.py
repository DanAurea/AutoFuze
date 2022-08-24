from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd

class TransportLayerCmdRequest(Cmd):
    """
    This class describes a connect request.
    """
    PID = StandardCommandCode.TRANSPORT_LAYER_CMD
    
    def __init__(self):
        self._sub_command_code = 0xFF
        self._parameters       = bytearray()