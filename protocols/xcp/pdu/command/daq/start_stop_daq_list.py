from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode

class StartStopDaqListRequest(object):
    
    def __init__(self):
        self._code            = DataAcquisitionCommand.START_STOP_DAQ_LIST
        self._mode            = 0xFF
        self._daq_list_number = 0xFF

class StartStopDaqListResponse(object):
    
    def __init__(self):
        self._code      = StandardCommandCode.CONNECT
        self._first_pid = 0xFF