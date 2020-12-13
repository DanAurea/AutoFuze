from xcp.enum.command_code import StandardCommandCode

class GetIdResponse(object):
    
    def __init__(self):
        self._code           = StandardCommandCode.CONNECT
        self._mode           = 0xFF
        self._length         = 0xFF
        self._identification = 0xFF