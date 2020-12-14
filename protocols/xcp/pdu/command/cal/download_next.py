from xcp.enum.command_code import CalibrationCommandCode
from xcp.enum.error_code import ErrorCode

from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.err import Err

class DownloadNextRequest(Cmd):
    
    def __init__(self):
        self._code                   = CalibrationCommandCode.DOWNLOAD_NEXT
        self._number_of_data_element = 0xFF
        self._alignment              = 0xFF
        self._data_element           = bytearray()

        super(DownloadNextRequest, self).__init__(pid = self._code)

class DownloadNextResponse(Err):
    
    def __init__(self):
        self._code                             = ErrorCode.ERR_SEQUENCE
        self._number_of_expected_data_element = 0xFF