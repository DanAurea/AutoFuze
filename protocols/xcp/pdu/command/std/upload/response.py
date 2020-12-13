from xcp.enum.command_code import StandardCommandCode

class UploadResponse(object):
    
    def __init__(self):
        self._code      = StandardCommandCode.CONNECT
        self._alignment = 0xFF
        self._elements  = bytearray()