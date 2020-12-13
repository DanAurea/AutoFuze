from xcp.enum.command_code import StandardCommandCode

class GetIdRequest(object):
    
    def __init__(self):
        self._code                          = StandardCommandCode.GET_ID
        self._requested_identification_type = 0xFF