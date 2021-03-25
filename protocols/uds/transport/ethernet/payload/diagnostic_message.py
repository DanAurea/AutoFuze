import sys

sys.path.append("../")
sys.path.append("../../")

from ctypes import BigEndianStructure, c_uint16, sizeof
from uds.transport.ethernet.message import DoIPMessage

class DiagnosticMessage(DoIPMessage):
    """
    This class describes a unified diagnostic message (UDS) over Ethernet.

    Inherits from DoIPMessage so DoIP header is automatically prepended.
    
    This is a generic message and should be used as it is, a convenient way
    to create quickly UDS message that will be sent/received over DoIP client.

    """
    _pack_   = 1
    _fields_ = [
                    ("source_address", c_uint16),
                    ("target_address", c_uint16)
                    #(data  * c_byte) Variable data length
                ]

    def __init__(self, source_address = 0x0000, target_address = 0x0000):
        super(DiagnosticMessage, self).__init__()
        self.source_address = source_address
        self.target_address = target_address

    def __repr__(self):
        s = '''{}\rPayload:
                    \r\tSource address : {}
                    \r\tTarget address : {}
            '''.format  (
                            super().__repr__(),
                            hex(self.source_address),
                            hex(self.target_address)
                        )

        return s