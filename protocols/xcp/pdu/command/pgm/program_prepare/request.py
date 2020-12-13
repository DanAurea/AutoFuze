from xcp.enum.command_code import NvmProgrammingCommand

class ProgramPrepareRequest(object):

    def __init__(self):
        self._code      = NvmProgrammingCommand.PROGRAM_PREPARE
        self._code_size = 0xFF