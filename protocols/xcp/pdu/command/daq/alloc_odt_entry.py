from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class AllocOdtEntryRequest(Cmd):
    PID = DataAcquisitionCommand.ALLOC_ODT_ENTRY
    
    def __init__(self):
        self._daq_list_number   = 0xFF
        self._odt_number        = 0xFF
        self._odt_entries_count = 0xFF