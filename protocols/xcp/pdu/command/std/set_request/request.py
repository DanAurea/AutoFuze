from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import SetRequestBit

class SetRequest(object):
    
    def __init__(self):
        self._code                     = StandardCommandCode.SET_REQUEST
        self._mode                     = SetRequestBit(0xFF)
        self._session_configuration_id = 0xFF