from xcp.pdu.base import XCPPacketBase

class Cmd(XCPPacketBase):
    
    def __init__(self, pid = 0xC0):
        super(Cmd, self).__init__(pid = pid)

    def is_correct_pid(self):
        correct = False

        if 0xC0 <= pid <= 0xFF:
            correct = True
        
        return correct