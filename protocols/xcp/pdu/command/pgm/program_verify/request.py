from xcp.enum.command_code import NvmProgrammingCommand

class ProgramVerifyRequest(object):

    def __init__(self):
        self._code               = NvmProgrammingCommand.PROGRAM_VERIFY
        self._verification_mode  = 0xFF
        self._verification_type  = 0xFF
        self._verification_value = 0xFF