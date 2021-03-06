from xcp.pdu.base import XCPPacketBase

class Err(XCPPacketBase):
    __slots__ = ("_code")
    
    def __init__(self):
        super(Err, self).__init__(pid = 0xFE)
        self._code                          = 0x0
        self.data                           = b''