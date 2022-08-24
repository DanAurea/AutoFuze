from xcp.enum.error_code import ErrorCode
from xcp.pdu.cto.base import XCPCTOCodeBase

class Err(XCPCTOCodeBase):
    __slots__ = ("code")
    
    PID = 0xFE
    CODE = ErrorCode.ERR_CMD_SYNCH

    def __init__(self, data = b''):
        self.data  = data