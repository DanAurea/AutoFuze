from xcp.enum.command_code import PageSwitchingCommand

class GetSegmentInfoRequest(object):

    def __init__(self):
        self._code           = PageSwitchingCommand.GET_SEGMENT_INFO
        self._mode           = 0xFF
        self._segment_number = 0xFF
        self._segment_info   = 0xFF
        self._mapping_index  = 0xFF