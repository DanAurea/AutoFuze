from xcp.enum.command_code import StandardCommandCode
from xcp.enum.error_code import ErrorCode

class ProgramNextResponse(object):

    def __init__(self):
        self._code                         = StandardCommandCode.DISCONNECT
        self._err                          = ErrorCode.ERR_SEQUENCE
        self._number_expected_data_element = 0xFF