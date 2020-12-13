from xcp.enum.command_code import CalibrationCommandCode

class ModifyBitsRequest(object):
    
    def __init__(self):
        self._code        = CalibrationCommandCode.MODIFY_BITS
        self._shift_value = 0xFF
        self._and_mask    = 0xFF
        self._or_mask     = 0xFF