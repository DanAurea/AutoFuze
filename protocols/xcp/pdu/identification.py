from struct import pack

from xcp.pdu.base import XCPPacketBase

class Identification(XCPPacketBase):
    """
    This class describes the identification field used in XCP frame.
    
    This field allow to identify nature of XCP packet sent between
    Master and Slave during XCP session.

    """
    def __init__(self, fill = 0x00, daq = None):
        self.fill = fill
        self.daq  = daq

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : PID
        [1:2] : Fill (Optional)
        [2:3] : DAQ (Optional)
        """
        class Payload(XCPPacketBase):
            _pack_   = 1
            _fields_ =  [
                        ]

        payload = Payload()

        return bytes(payload)