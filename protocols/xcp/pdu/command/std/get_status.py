from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CurrentSessionStatusBit, RessourceBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetStatusRequest(Cmd):
    """
    This class describes a get current session request.
    """
    PID = StandardCommandCode.GET_STATUS

class GetStatusResponse(Res):
    """
    This class describes a get current session request.
    """
    PID = StandardCommandCode.CONNECT

    def __init__(self):
        self._session_status             = CurrentSessionStatusBit(0xFF)
        self._resource_protection_status = RessourceBit(0xFF)
        self._session_configuration_id   = 0xFF