from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetIdRequest(Cmd):
    PID = StandardCommandCode.GET_ID
    
    def __init__(self):
        self._requested_identification_type = 0xFF

class GetIdResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._mode           = 0xFF
        self._length         = 0xFF
        self._identification = 0xFF