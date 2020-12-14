from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class ModifyBitsRequest(Cmd):
    
    def __init__(self):
        self._code        = CalibrationCommandCode.MODIFY_BITS
        self._shift_value = 0xFF
        self._and_mask    = 0xFF
        self._or_mask     = 0xFF

        super(ModifyBitsRequest, self).__init__(pid = self._code)