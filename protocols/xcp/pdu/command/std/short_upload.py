from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd

class ShortUploadRequest(Cmd):
    PID = StandardCommandCode.SHORT_UPLOAD
    
    def __init__(self):
        self._number_of_data_element = 0xFF
        self._address_extension      = bytearray()
        self._address                = bytearray()