from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetSegmentModeBit

class GetSegmentModeRequest(object):

    def __init__(self):
        self._code           = PageSwitchingCommand.GET_SEGMENT_MODE
        self._segment_number = 0xFF

class GetSegmentModeResponse(object):

    def __init__(self):
        self._code = StandardCommandCode.CONNECT
        self._mode = GetSegmentModeBit(0xFF)  