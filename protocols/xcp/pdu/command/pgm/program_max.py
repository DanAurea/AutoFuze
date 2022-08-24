from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramMaxRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM_MAX

    def __init__(self):
        self._alignment    = 0xFF
        self._data_element = bytearray()