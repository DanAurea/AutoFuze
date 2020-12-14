from xcp.enum.command_code import StandardCommandCode

class GetSeedRequest(object):
    
    def __init__(self):
        self._code     = StandardCommandCode.GET_SEED
        self._mode     = 0xFF
        self._resource = 0xFF

class GetSeedResponse(object):
    
    def __init__(self):
        self._code   = StandardCommandCode.CONNECT
        self._length = 0xFF
        self._seed   = 0xFF