from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CommModeOptionalBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetCommModeInfo(Cmd):
    PID = StandardCommandCode.GET_COMM_MODE_INFO

class GetCommModeInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._comm_mode_optional       = CommModeOptionalBit(0xFF)
        self._max_bs                   = 0xFF
        self._min_st                   = 0xFF
        self._queue_size               = 0xFF
        self._xcp_drive_version_number = 0xFF