from xcp.enum.command_code import NvmProgrammingCommand

class ProgramStartRequest(object):
    
    def __init__(self):
        self._code = NvmProgrammingCommand.PROGRAM_START