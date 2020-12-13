from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CommModeOptionalBit

class GetCommModeInfo(object):
    
    def __init__(self):
        self._code                     = StandardCommandCode.CONNECT
        self._comm_mode_optional       = CommModeOptionalBit(0xFF)
        self._max_bs                   = 0xFF
        self._min_st                   = 0xFF
        self._queue_size               = 0xFF
        self._xcp_drive_version_number = 0xFF