from xcp.enum.command_code import CalibrationCommandCode

class DownloadMaxRequest(object):
    
    def __init__(self):
        self._code          = CalibrationCommandCode.DOWNLOAD_MAX
        self._alignment     = 0xFF
        self._data_elements = bytearray()