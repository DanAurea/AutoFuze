from xcp.pdu.dto.base import XCPDTOBase

class STIM(XCPDTOBase):

    def is_correct_pid(self):
        correct = False

        if 0x00 <= self.pid <= 0xBF:
            correct = True

        return correct