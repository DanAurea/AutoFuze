from xcp.enum.command_code import DataAcquisitionCommand

class FreeDaqRequest(object):
    
    def __init__(self):
        self._code = DataAcquisitionCommand.FREE_DAQ