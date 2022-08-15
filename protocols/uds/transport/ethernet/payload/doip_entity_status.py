from ctypes import c_uint8, c_uint32

from uds.transport.ethernet.enum.connection_kind import ConnectionKind
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.message import DoIPMessage

class DoIPEntityStatusRequest(DoIPMessage):
    """
    Ask information about status of DoIP node.
    Response give information on
    """
    _pack_   = 1
    _fields_ =  [
                ]
    
    CONNECTION_KIND = ConnectionKind.UDP
    PAYLOAD_TYPE    = DoIPPayloadType.DOIP_ENTITY_STATUS_REQUEST

    def __init__(self):
        super(DoIPEntityStatusRequest, self).__init__()

class DoIPEntityStatusResponse(DoIPMessage):
    """
    Reponse of DoIP node about its status.
    """
    _pack_   = 1
    _fields_ =  [
                    ("node_type", c_uint8),
                    ("max_open_sockets", c_uint8),
                    ("currently_open_socket", c_uint8),
                    ("max_data_size", c_uint32),
                ]
    
    CONNECTION_KIND = ConnectionKind.UDP
    PAYLOAD_TYPE    = DoIPPayloadType.DOIP_ENTITY_STATUS_RESPONSE

    def __init__(self):
        super(DoIPEntityStatusResponse, self).__init__()

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tNode type: {}
                    \r\tMax open sockets: {}
                    \r\tCurrently open socket: {}
                    \r\tMax data size: {}
            """.format  (
                            super(DoIPEntityStatusResponse, self).__repr__(),
                            self.max_open_sockets,
                            self.currently_open_socket,
                            self.max_data_size,
                        )

        return s