from xcp.enum.command_code import DataAcquisitionCommand

class ClearDaqListRequest(object):
    
    def __init__(self):
        self._code            = DataAcquisitionCommand.CLEAR_DAQ_LIST
        self._daq_list_number = 0xFF