from xcp.pdu.base import Base

class Cmd(Base):
    
    def __init__(self):
        super(Cmd, self).__init__(pid = 0xC0)
        self.data = b''

    def is_correct_pid(self):
        correct = False

        if 0xC0 <= pid <= 0xFF:
            correct = True
        
        return correct