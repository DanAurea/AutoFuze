from xcp.enum.command_code import PageSwitchingCommand

class GetPageInfoRequest(object):
    
    def __init__(self):
        self._code           = PageSwitchingCommand.GET_PAGE_INFO
        self._segment_number = 0xFF
        self._page_number    = 0xFF