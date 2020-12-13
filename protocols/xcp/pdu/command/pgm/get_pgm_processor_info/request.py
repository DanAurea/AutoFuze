from xcp.enum.command_code import NvmProgrammingCommand

class GetPgmProcessorInfoRequest(object):
    
    def __init__(self):
        self._code = NvmProgrammingCommand.GET_PGM_PROCESSOR_INFO