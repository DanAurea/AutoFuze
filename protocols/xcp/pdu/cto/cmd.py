from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.base import XCPPacketBase

class Cmd(XCPPacketBase):
    PID = StandardCommandCode.CONNECT

    def is_correct_pid(self):
        correct = False

        if 0xC0 <= pid <= 0xFF:
            correct = True
        
        return correct