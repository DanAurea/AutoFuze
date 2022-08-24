from xcp.enum.command_code import StandardCommandCode
from xcp.enum.error_code import ErrorCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class SynchRequest(Cmd):
    """
    This class describes a connect request.
    """
    PID = StandardCommandCode.SYNCH

class SynchResponse(Res):
    """
    This class describes a connect request.
    """
    PID = StandardCommandCode.DISCONNECT
    
    def __init__(self):
        self._err  = ErrorCode.ERR_CMD_SYNCH