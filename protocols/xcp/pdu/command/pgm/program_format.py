from xcp.enum.command_code import NvmProgrammingCommand

class ProgramFormatRequest(object):

    def __init__(self):
        self._code               = NvmProgrammingCommand.PROGRAM_FORMAT
        self._compression_method = 0xFF
        self._encryption_method  = 0xFF
        self._programming_method = 0xFF
        self._access_method      = 0xFF