from xcp.enum.command_code import DataAcquisitionCommand

class GetDaqResolutionInfoRequest(object):
    
    def __init__(self):
        self._code = DataAcquisitionCommand.DAQ_RESOLUTION_INFO