from ctypes import c_uint8, c_uint16, c_uint32

from xcp.enum.command_code import StandardCommandCode
from xcp.enum.checksum_type import ChecksumType
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class BuildChecksum(Cmd):
    PID = StandardCommandCode.BUILD_CHECKSUM
        
    _pack_   = 1
    _fields_ =  [
                    ('reserved', 3* c_uint8),
                    ('block_size', c_uint32),
                ]

    def __init__(self, block_size = 0xFF):
        self.block_size = block_size

class BuildChecksumResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    # TODO: Handle positive/negative response
    _pack_   = 1
    _fields_ =  [
                    ('checksum_type', c_uint8),
                    ('reserved', c_uint16),
                    ('checksum', c_uint32),
                ]

    def __init__(self):
        self.err                = StandardCommandCode.DISCONNECT
        self.checksum_type      = ChecksumType(0xFF)
        self.checksum           = 0xFF
        self.maximum_block_size = 0xFF        