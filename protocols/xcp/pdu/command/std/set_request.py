from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import SetRequestBit
from xcp.pdu.cto.cmd import Cmd

class SetRequest(Cmd):
    PID = StandardCommandCode.SET_REQUEST
    
    def __init__(self):
        self._mode                     = SetRequestBit(0xFF)
        self._session_configuration_id = 0xFF