from xcp.enum.command_code import CalibrationCommandCode

class DownloadNextRequest(object):
    
    def __init__(self):
        self._code                   = CalibrationCommandCode.DOWNLOAD_NEXT
        self._number_of_data_element = 0xFF
        self._alignment              = 0xFF
        self._data_element           = bytearray()