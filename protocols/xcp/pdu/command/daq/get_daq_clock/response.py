from xcp.enum.command_code import StandardCommandCode

class GetDaqClockResponse(object):
    
    def __init__(self):
        self._code              = StandardCommandCode.CONNECT
        self._receive_timestamp = 0xFF