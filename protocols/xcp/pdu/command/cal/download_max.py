from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class DownloadMaxRequest(Cmd):
    
    def __init__(self):
        self._code          = CalibrationCommandCode.DOWNLOAD_MAX
        self._alignment     = 0xFF
        self._data_elements = bytearray()

        super(DownloadMaxRequest, self).__init__(pid = self._code)