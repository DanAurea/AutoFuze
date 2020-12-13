from xcp.enum.command_code import DataAcquisitionCommand

class StartStopSynchRequest(object):
    
    def __init__(self):
        self._code = DataAcquisitionCommand.START_STOP_SYNCH
        self._mode = 0xFF