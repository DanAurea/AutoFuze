from xcp.enum.command_code import StandardCommandCode

class GetIdRequest(object):
    
    def __init__(self):
        self._code                          = StandardCommandCode.GET_ID
        self._requested_identification_type = 0xFF

class GetIdResponse(object):
    
    def __init__(self):
        self._code           = StandardCommandCode.CONNECT
        self._mode           = 0xFF
        self._length         = 0xFF
        self._identification = 0xFF