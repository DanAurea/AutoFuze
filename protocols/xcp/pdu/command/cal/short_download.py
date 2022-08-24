from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class ShortDownloadRequest(Cmd):
    PID = CalibrationCommandCode.SHORT_DOWNLOAD
    
    def __init__(self):
        self._number_of_data_element = 0xFF
        self._address_extension      = 0xFF
        self._address                = 0xFF
        self._data_elements          = bytearray()