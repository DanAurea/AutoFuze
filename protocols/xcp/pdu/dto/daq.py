from xcp.pdu.base import XCPPacketBase
from xcp.pdu.identification import Identification

class Daq(XCPPacketBase):
    
    def __init__(self):
        super(Daq, self).__init__(pid = 0x00)
        self.identification = Identification()
        self.data = b'' 

    def is_correct_pid(self):
        correct = False

        if 0x00 <= self.pid <= 0xFB:
            correct = True

        return correct