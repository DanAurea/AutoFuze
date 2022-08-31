from xcp.pdu.cto.base import XCPCTOBase

class Cmd(XCPCTOBase):

    def is_correct_pid(self):
        correct = False

        if 0xC0 <= pid <= 0xFF:
            correct = True
        
        return correct