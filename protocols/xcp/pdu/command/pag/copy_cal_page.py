from xcp.enum.command_code import PageSwitchingCommand

class CopyCalPageRequest(object):

    def __init__(self):
        self._code                                    = PageSwitchingCommand.COPY_CAL_PAGE
        self._logical_data_segment_number_source      = 0xFF
        self._logical_data_page_number_source         = 0xFF
        self._logical_data_segment_number_destination = 0xFF
        self._logical_data_page_number_destination    = 0xFF