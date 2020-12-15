from xcp.pdu.base import PacketBase
from xcp.pdu.identification import Identification

class Stim(PacketBase):
    
    def __init__(self):
        super(Stim, self).__init__(pid = 0x00)
        self.identification = Identification()
        self.data = b''

    def is_correct_pid(self):
        correct = False

        if 0x00 <= self.pid <= 0xBF:
            correct = True

        return correct