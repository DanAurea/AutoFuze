from xcp.enum.command_code import StandardCommandCode

class GetCommModeInfo(object):
    
    def __init__(self):
        self._code = StandardCommandCode.GET_COMM_MODE_INFO