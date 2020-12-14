from xcp.enum.command_code import DataAcquisitionCommand

class AllocOdtEntryRequest(object):
    
    def __init__(self):
        self._code              = DataAcquisitionCommand.ALLOC_ODT_ENTRY
        self._daq_list_number   = 0xFF
        self._odt_number        = 0xFF
        self._odt_entries_count = 0xFF