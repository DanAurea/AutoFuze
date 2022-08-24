from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class AllocDaqRequest(Cmd):
    PID = DataAcquisitionCommand.ALLOC_DAQ
    
    def __init__(self):
        self._daq_count = 0xFF