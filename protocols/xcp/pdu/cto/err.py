from xcp.enum.error_code import ErrorCode
from xcp.pdu.cto.base import XCPCTOBase

class Err(XCPCTOBase):
    __slots__ = ("code")
    
    PID  = 0xFE

    def __init__(self, code = ErrorCode.ERR_CMD_SYNCH, data = b''):
        self.code  = code
        self.data  = data