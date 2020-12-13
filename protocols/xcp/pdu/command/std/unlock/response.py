from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CurrentSessionStatusBit

class UnlockResponse(object):
    
    def __init__(self):
        self._code                       = StandardCommandCode.CONNECT
        self._resource_protection_status = CurrentSessionStatusBit(0xFF)