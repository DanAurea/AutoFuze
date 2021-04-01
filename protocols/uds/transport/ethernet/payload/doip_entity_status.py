from ctypes import c_uint8, c_uint32

from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class DoIPEntityStatusRequest(DoIPMessage):
    """
    Ask information about status of DoIP node.
    Response give information on
    """
    _pack_   = 1
    _fields_ =  [
                ]
    
    def __init__(self):
        super(DoIPEntityStatusRequest, self).__init__(payload_type = DoIPPayloadType.DOIP_ENTITY_STATUS_REQUEST)

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
    
    def __init__(self):
        super(DoIPEntityStatusResponse, self).__init__(payload_type = DoIPPayloadType.DOIP_ENTITY_STATUS_RESPONSE)