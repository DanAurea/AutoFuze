from xcp.enum.command_code import NvmProgrammingCommand

class ProgramClearRequest(object):
    
    def __init__(self):
        self._code        = NvmProgrammingCommand.PROGRAM_CLEAR
        self._mode        = 0xFF
        self._clear_range = 0xFFFF