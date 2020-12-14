from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CurrentSessionStatusBit, RessourceBit

class GetStatusRequest(object):
    """
    This class describes a get current session request.
    """

    def __init__(self):
        self._code = StandardCommandCode.GET_STATUS

class GetStatusResponse(object):
    """
    This class describes a get current session request.
    """

    def __init__(self):
        self._pid                        = StandardCommandCode.CONNECT
        self._session_status             = CurrentSessionStatusBit(0xFF)
        self._resource_protection_status = RessourceBit(0xFF)
        self._session_configuration_id   = 0xFF