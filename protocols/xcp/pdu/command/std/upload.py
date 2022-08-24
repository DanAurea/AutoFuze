from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class UploadRequest(Cmd):
    PID = StandardCommandCode.UPLOAD
    
    def __init__(self):
        self._number_of_data_element = 0xFF

class UploadResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._alignment = 0xFF
        self._elements  = bytearray()