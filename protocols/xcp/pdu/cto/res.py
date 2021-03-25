from xcp.pdu.base import XCPPacketBase

class Res(XCPPacketBase):
    
    def __init__(self):
        super(Res, self).__init__(pid = 0xFF)