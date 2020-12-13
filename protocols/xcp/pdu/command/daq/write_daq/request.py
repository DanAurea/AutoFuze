from xcp.enum.command_code import DataAcquisitionCommand

class WriteDaqRequest(object):
    
    def __init__(self):
        self._code                = DataAcquisitionCommand.WRITE_DAQ
        self._bit_offset          = 0xFF
        self._size_of_daq_element = 0xFF
        self._address_extension   = 0xFF
        self._address             = 0xFF