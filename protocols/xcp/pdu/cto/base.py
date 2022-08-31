from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.base import XCPPacketBase
from xcp.pdu.identification import Identification
from xcp.pdu.timestamp import Timestamp

class XCPCTOBase(XCPPacketBase):
    PID = StandardCommandCode.CONNECT

    def __new__(cls, *args, **kwargs):
        instance                = super(XCPCTOBase, cls).__new__(cls, *args, **kwargs)
        instance.identification = Identification(cls.PID)
        instance.timestamp      = Timestamp() # Timestamp is empty in CMD

        return instance