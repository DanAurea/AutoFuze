from xcp.enum.command_code import StandardCommandCode

class GetSeedResponse(object):
    
    def __init__(self):
        self._code   = StandardCommandCode.CONNECT
        self._length = 0xFF
        self._seed   = 0xFF