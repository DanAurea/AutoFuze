from xcp.enum.event_code import EventCode
from xcp.pdu.cto.base import XCPCTOCodeBase

class Ev(XCPCTOCodeBase):
    PID  = 0xFD
    CODE = EventCode.EV_RESUME_MODE

    def __init__(self, data = b''):
        self.data = data