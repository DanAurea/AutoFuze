from xcp.enum.command_code import PageSwitchingCommand

class GetSegmentModeRequest(object):

    def __init__(self):
        self._code           = PageSwitchingCommand.GET_SEGMENT_MODE
        self._segment_number = 0xFF  