from xcp.enum.command_code import StandardCommandCode

class ShortUploadRequest(object):
    
    def __init__(self):
        self._code                   = StandardCommandCode.SHORT_UPLOAD
        self._number_of_data_element = 0xFF
        self._address_extension      = bytearray()
        self._address                = bytearray()