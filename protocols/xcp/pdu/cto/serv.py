from xcp.pdu.base import XCPPacketBase

class Serv(XCPPacketBase):
    
    def __init__(self):
        super(Serv, self).__init__(pid = 0xFC)
        self.service_request_code = 0x0
        self.data = 0x0