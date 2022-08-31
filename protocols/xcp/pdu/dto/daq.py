from xcp.pdu.dto.base import XCPDTOBase

class DAQ(XCPDTOBase):

    def is_correct_pid(self):
        correct = False

        if 0x00 <= self.pid <= 0xFB:
            correct = True

        return correct