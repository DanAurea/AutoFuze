from ctypes import c_uint8

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
    
    _pack_   = 1
    _fields_ =  [
                    ('err', c_uint8),
                ]

    def __init__(self):
        self.err  = ErrorCode.ERR_CMD_SYNCH