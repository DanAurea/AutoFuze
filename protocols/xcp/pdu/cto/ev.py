from xcp.enum.event_code import EventCode
from xcp.pdu.cto.base import XCPCTOBase

class Ev(XCPCTOBase):
    PID  = 0xFD

    def __init__(self, code = EventCode.EV_RESUME_MODE, data = b''):
        self.code = code
        self.data = data