from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class StartStopSynchRequest(Cmd):
    PID = DataAcquisitionCommand.START_STOP_SYNCH
    
    def __init__(self):
        self._mode = 0xFF