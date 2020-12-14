from xcp.enum.command_code import DataAcquisitionCommand

class AllocOdtRequest(object):
    
    def __init__(self):
        self._code            = DataAcquisitionCommand.ALLOC_ODT
        self._daq_list_number = 0xFF
        self._odt_count       = 0xFF