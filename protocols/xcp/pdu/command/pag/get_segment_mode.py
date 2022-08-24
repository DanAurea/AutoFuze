from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetSegmentModeBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSegmentModeRequest(Cmd):
    PID = PageSwitchingCommand.GET_SEGMENT_MODE

    def __init__(self):
        self._segment_number = 0xFF

class GetSegmentModeResponse(Res):
    PID = StandardCommandCode.CONNECT

    def __init__(self):
        self._mode = GetSegmentModeBit(0xFF)  