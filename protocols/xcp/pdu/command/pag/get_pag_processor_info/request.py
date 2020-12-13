from xcp.enum.command_code import PageSwitchingCommand

class GetPagProcessorInfoRequest(object):
    
    def __init__(self):
        self._code  = PageSwitchingCommand.GET_PAG_PROCESSOR_INFO