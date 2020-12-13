from xcp.enum.command_code import DataAcquisitionCommand

class GetDaqClockRequest(object):
    
    def __init__(self):
        self._code = DataAcquisitionCommand.GET_DAQ_CLOCK