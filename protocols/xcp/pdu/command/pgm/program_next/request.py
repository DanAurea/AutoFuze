from xcp.enum.command_code import NvmProgrammingCommand

class ProgramNextRequest(object):

    def __init__(self):
        self._code                = NvmProgrammingCommand.PROGRAM_NEXT
        self._number_data_element = 0xFF
        self._alignment           = 0xFF
        self._data_element        = bytearray()