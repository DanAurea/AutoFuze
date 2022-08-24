from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CurrentSessionStatusBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class UnlockRequest(Cmd):
    PID = StandardCommandCode.UNLOCK
    
    def __init__(self):
        self._length = 0xFF
        self._key    = 0xFF

class UnlockResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._resource_protection_status = CurrentSessionStatusBit(0xFF)