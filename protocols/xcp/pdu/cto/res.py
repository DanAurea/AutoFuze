from xcp.pdu.base import PacketBase

class Res(Base):
    
    def __init__(self):
        super(Res, self).__init__(pid = 0xFF)