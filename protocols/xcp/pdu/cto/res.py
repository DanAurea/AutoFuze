from xcp.pdu.cto.base import XCPCTOBase

class Res(XCPCTOBase):
    PID  = 0xFF

    def __init__(self, code = 0xFF):
        self.code = code