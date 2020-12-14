from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.parameter_bit import SetSegmentModeBit

class SetSegmentModeRequest(object):

    def __init__(self):
        self._code           = PageSwitchingCommand.SET_SEGMENT_MODE
        self._mode           = SetSegmentModeBit(0xFF)
        self._segment_number = 0xFF