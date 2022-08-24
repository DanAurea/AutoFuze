from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class AllocOdtRequest(Cmd):
    PID = DataAcquisitionCommand.ALLOC_ODT
    
    def __init__(self):
        self._daq_list_number = 0xFF
        self._odt_count       = 0xFF