from ctypes import c_uint16, sizeof

from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class AliveCheckRequest(DoIPMessage):
    """
    Can be sent before closing socket to ensure node is still alive or not.
    """
    _pack_   = 1
    _fields_ =  [
                ]
    
    def __init__(self):
        super(AliveCheckRequest, self).__init__(payload_type = DoIPPayloadType.ALIVE_CHECK_REQUEST)

class AliveCheckResponse(DoIPMessage):
    """
    Alive check ACK.
    
    If source address doesn't match with the registered source address of the connection then socket
    should be closed.
    """
    _pack_   = 1
    _fields_ =  [
                    ("source_address", c_uint16)
                ]

    def __init__(self):
        super(AliveCheckResponse, self).__init__(payload_type = DoIPPayloadType.ALIVE_CHECK_RESPONSE)

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tSource address: {}
            """.format  (
                            super(AliveCheckResponse, self).__repr__(),
                            hex(self.source_address),
                        )       

        return s