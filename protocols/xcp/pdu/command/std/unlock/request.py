from xcp.enum.command_code import StandardCommandCode

class UnlockRequest(object):
    
    def __init__(self):
        self._code   = StandardCommandCode.UNLOCK
        self._length = 0xFF
        self._key    = 0xFF