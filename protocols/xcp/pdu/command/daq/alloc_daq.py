from xcp.enum.command_code import DataAcquisitionCommand

class AllocDaqRequest(object):
    
    def __init__(self):
        self._code      = DataAcquisitionCommand.ALLOC_DAQ
        self._daq_count = 0xFF