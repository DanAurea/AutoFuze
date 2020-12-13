from xcp.enum.command_code import NvmProgrammingCommand

class GetSectorInfoRequest(object):

    def __init__(self):
        self._code          = NvmProgrammingCommand.GET_SECTOR_INFO
        self._mode          = 0xFF
        self._sector_number = 0xFF