from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class ModifyBitsRequest(Cmd):
    PID = CalibrationCommandCode.MODIFY_BITS
    
    def __init__(self):
        self._shift_value = 0xFF
        self._and_mask    = 0xFF
        self._or_mask     = 0xFF