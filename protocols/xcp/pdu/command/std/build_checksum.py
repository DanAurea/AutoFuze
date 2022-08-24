from xcp.enum.command_code import StandardCommandCode
from xcp.enum.checksum_type import ChecksumType
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class BuildChecksumRequest(Cmd):
    PID = StandardCommandCode.BUILD_CHECKSUM
    
    def __init__(self):
        self._block_size = 0xFF

class BuildChecksumResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._err                = StandardCommandCode.DISCONNECT
        self._checksum_type      = ChecksumType(0xFF)
        self._checksum           = 0xFF
        self._maximum_block_size = 0xFF