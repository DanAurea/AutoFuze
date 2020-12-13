from xcp.enum.command_code import StandardCommandCode

class StartStopDaqListResponse(object):
    
    def __init__(self):
        self._code      = StandardCommandCode.CONNECT
        self._first_pid = 0xFF