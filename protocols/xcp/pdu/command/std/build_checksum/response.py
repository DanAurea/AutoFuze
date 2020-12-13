from xcp.enum.command_code import StandardCommandCode
from xcp.enum.checksum_type import ChecksumType

class BuildChecksumResponse(object):
    
    def __init__(self):
        self._code               = StandardCommandCode.CONNECT
        self._err                = StandardCommandCode.DISCONNECT
        self._checksum_type      = ChecksumType(0xFF)
        self._checksum           = 0xFF
        self._maximum_block_size = 0xFF