from xcp.enum.command_code import DataAcquisitionCommand

class SetDaqPtrRequest(object):
    
    def __init__(self):
        self._code             = DataAcquisitionCommand.SET_DAQ_PTR
        self._daq_list_number  = 0xFF
        self._odt_number       = 0xFF
        self._odt_entry_number = 0xFF