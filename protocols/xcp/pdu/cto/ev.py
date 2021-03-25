from xcp.pdu.base import XCPPacketBase

class Ev(XCPPacketBase):
    
    def __init__(self):
        super(Ev, self).__init__(pid = 0xFD)
        self.code = 0x0
        self.data = b''