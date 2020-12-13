from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetSegmentModeBit

class GetSegmentModeResponse(object):

    def __init__(self):
        self._code = StandardCommandCode.CONNECT
        self._mode = GetSegmentModeBit(0xFF)  