from xcp.enum.service_request_code import ServiceRequestCode
from xcp.pdu.cto.base import XCPCTOBase

class Serv(XCPCTOBase):
    PID = 0xFC
    
    def __init__(self, code = ServiceRequestCode.SERV_RESET, data = b''):
        self.code = code
        self.data = data