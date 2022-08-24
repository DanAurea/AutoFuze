from xcp.enum.command_code import CalibrationCommandCode
from xcp.enum.error_code import ErrorCode

from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.err import Err

class DownloadNextRequest(Cmd):
    PID = CalibrationCommandCode.DOWNLOAD_NEXT

    def __init__(self):
        self._number_of_data_element = 0xFF
        self._alignment              = 0xFF
        self._data_element           = bytearray()

class DownloadNextResponse(Err):
    
    def __init__(self):
        self.code                             = ErrorCode.ERR_SEQUENCE
        self._number_of_expected_data_element = 0xFF