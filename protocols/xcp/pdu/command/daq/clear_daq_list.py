from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class ClearDaqListRequest(Cmd):
    PID = DataAcquisitionCommand.CLEAR_DAQ_LIST
    
    def __init__(self):
        self._daq_list_number = 0xFF