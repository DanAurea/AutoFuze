from xcp.enum.command_code import StandardCommandCode

class UploadRequest(object):
    
    def __init__(self):
        self._code                   = StandardCommandCode.UPLOAD
        self._number_of_data_element = 0xFF