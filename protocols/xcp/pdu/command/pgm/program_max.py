from xcp.enum.command_code import NvmProgrammingCommand

class ProgramMaxRequest(object):

    def __init__(self):
        self._code         = NvmProgrammingCommand.PROGRAM_MAX
        self._alignment    = 0xFF
        self._data_element = bytearray()