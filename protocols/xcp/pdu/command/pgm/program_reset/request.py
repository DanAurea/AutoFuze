from xcp.enum.command_code import NvmProgrammingCommand

class ProgramResetRequest(object):
    
    def __init__(self):
        self._code                = NvmProgrammingCommand.PROGRAM_RESET