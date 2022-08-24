from xcp.enum.command_code import PageSwitchingCommand
from xcp.pdu.cto.cmd import Cmd

class CopyCalPageRequest(Cmd):
    PID = PageSwitchingCommand.COPY_CAL_PAGE

    def __init__(self):
        self._logical_data_segment_number_source      = 0xFF
        self._logical_data_page_number_source         = 0xFF
        self._logical_data_segment_number_destination = 0xFF
        self._logical_data_page_number_destination    = 0xFF