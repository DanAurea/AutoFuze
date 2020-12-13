from xcp.enum.command_code import CalibrationCommandCode

class ShortDownloadRequest(object):
    
    def __init__(self):
        self._code                   = CalibrationCommandCode.SHORT_DOWNLOAD
        self._number_of_data_element = 0xFF
        self._address_extension      = 0xFF
        self._address                = 0xFF
        self._data_elements          = bytearray()