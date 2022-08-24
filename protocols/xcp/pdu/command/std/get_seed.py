from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSeedRequest(Cmd):
    PID = StandardCommandCode.GET_SEED
    
    def __init__(self):
        self._mode     = 0xFF
        self._resource = 0xFF

class GetSeedResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._length = 0xFF
        self._seed   = 0xFF