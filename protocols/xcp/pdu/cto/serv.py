from xcp.enum.service_request_code import ServiceRequestCode
from xcp.pdu.cto.base import XCPCTOCodeBase

class Serv(XCPCTOCodeBase):
    PID = 0xFC
    CODE = ServiceRequestCode.SERV_RESET
    
    def __init__(self, data = b''):
        self.data = data