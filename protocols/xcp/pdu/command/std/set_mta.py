from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd

class SetMtaRequest(Cmd):
    PID = StandardCommandCode.SET_MTA
    
    def __init__(self):
        self._address_extension = 0xFF
        self._address           = 0xFF