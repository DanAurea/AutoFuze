from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode

class ReadDaqRequest(object):

    def __init__(self):
        self._code = DataAcquisitionCommand.READ_DAQ

class ReadDaqResponse(object):

    def __init__(self):
        self._code                = StandardCommandCode.CONNECT
        self._bit_offset          = 0xFF
        self._size_of_daq_element = 0xFF
        self._address_extension   = 0xFF
        self._address             = 0xFF