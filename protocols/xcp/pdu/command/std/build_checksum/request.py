from xcp.enum.command_code import StandardCommandCode

class BuildChecksumRequest(object):
    
    def __init__(self):
        self._code       = StandardCommandCode.BUILD_CHECKSUM
        self._block_size = 0xFF