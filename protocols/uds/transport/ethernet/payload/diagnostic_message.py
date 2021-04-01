from ctypes import c_uint16

from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

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
        super(DiagnosticMessage, self).__init__(payload_type = DoIPPayloadType.DIAGNOSTIC_MESSAGE)
        self.source_address = source_address
        self.target_address = target_address
        self.pdu            = None

    def __truediv__(self, pdu):
        """
        Override true division operator so packet crafting will be prettier.
        
        :param      payload:  The payload
        :type       payload:  PayloadType
        
        :returns:   The final DoIP message
        :rtype:     bytes
        """
        self.pdu = pdu
        return self

    def __bytes__(self):
        """
        Bytes representation of the final DoIP Message.

        DoIPHeader / Payload / PDU (if there's one) should all being concatenated.
        """
        b = bytearray(self) # Hack to avoid recursive call to __bytes__()

        if self.pdu:
            b += bytes(self.pdu)
        else:
            #TODO: Log warning PDU is empty
            pass
            
        return bytes(b)
    def __repr__(self):
        s = """{}\rPayload:
                    \r\tSource address : {}
                    \r\tTarget address : {}
            """.format  (
                            super().__repr__(),
                            hex(self.source_address),
                            hex(self.target_address)
                        )

        if self.payload:
            s = """{}\r{}""".format  (
                                s,
                                self.payload
                            )
        return s