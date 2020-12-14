from xcp.enum.command_code import StandardCommandCode
from xcp.enum.error_code import ErrorCode

class SynchRequest(object):
    """
    This class describes a connect request.
    """
    def __init__(self):
        self._code = StandardCommandCode.SYNCH

class SynchResponse(object):
    """
    This class describes a connect request.
    """
    def __init__(self):
        self._code = StandardCommandCode.DISCONNECT
        self._err  = ErrorCode.ERR_CMD_SYNCH