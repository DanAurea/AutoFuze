from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class DownloadMaxRequest(Cmd):
    PID = CalibrationCommandCode.DOWNLOAD_MAX

    def __init__(self):
        self._alignment     = 0xFF
        self._data_elements = bytearray()