from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class SetDaqPtrRequest(Cmd):
    PID = DataAcquisitionCommand.SET_DAQ_PTR
    
    def __init__(self):
        self._daq_list_number  = 0xFF
        self._odt_number       = 0xFF
        self._odt_entry_number = 0xFF