from xcp.enum.command_code import DataAcquisitionCommand

class GetDaqListInfoRequest(object):
    
    def __init__(self):
        self._code            = DataAcquisitionCommand.GET_DAQ_LIST_INFO
        self._daq_list_number = 0xFF