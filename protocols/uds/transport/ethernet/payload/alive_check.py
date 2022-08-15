from ctypes import c_uint16, sizeof

from uds.transport.ethernet.enum.connection_kind import ConnectionKind
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.message import DoIPMessage

class AliveCheckRequest(DoIPMessage):
    """
    Can be sent before closing socket to ensure node is still alive or not.
    """
    _pack_   = 1
    _fields_ =  [
                ]
    
    CONNECTION_KIND = ConnectionKind.TCP
    PAYLOAD_TYPE    = DoIPPayloadType.ALIVE_CHECK_REQUEST

    def __init__(self):
        super(AliveCheckRequest, self).__init__()

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

    CONNECTION_KIND = ConnectionKind.TCP
    PAYLOAD_TYPE    = DoIPPayloadType.ALIVE_CHECK_RESPONSE

    def __init__(self):
        super(AliveCheckResponse, self).__init__()

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tSource address: {}
            """.format  (
                            super(AliveCheckResponse, self).__repr__(),
                            hex(self.source_address),
                        )       

        return s