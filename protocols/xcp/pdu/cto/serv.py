from xcp.pdu.base import PacketBase

class Serv(Base):
    
    def __init__(self):
        super(Serv, self).__init__(pid = 0xFC)
        self.service_request_code = 0x0
        self.data = 0x0