from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CurrentSessionStatusBit

class UnlockRequest(object):
    
    def __init__(self):
        self._code   = StandardCommandCode.UNLOCK
        self._length = 0xFF
        self._key    = 0xFF

class UnlockResponse(object):
    
    def __init__(self):
        self._code                       = StandardCommandCode.CONNECT
        self._resource_protection_status = CurrentSessionStatusBit(0xFF)