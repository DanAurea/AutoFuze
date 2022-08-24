from xcp.enum.command_code import NvmProgrammingCommand
from xcp.pdu.cto.cmd import Cmd

class ProgramRequest(Cmd):
    PID = NvmProgrammingCommand.PROGRAM
    
    def __init__(self):
        self._number_data_element = 0xFF
        self._alignment           = 0xFF
        self._data_element        = bytearray()