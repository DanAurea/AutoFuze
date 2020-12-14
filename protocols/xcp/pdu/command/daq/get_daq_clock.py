from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode

class GetDaqClockRequest(object):
    
    def __init__(self):
        self._code = DataAcquisitionCommand.GET_DAQ_CLOCK

class GetDaqClockResponse(object):
    
    def __init__(self):
        self._code              = StandardCommandCode.CONNECT
        self._receive_timestamp = 0xFF