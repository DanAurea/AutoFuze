from ctypes import c_char, c_uint8, c_uint16
from struct import pack, unpack

from uds.transport.ethernet.enum.connection_kind import ConnectionKind
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.enum.routing_activation_type import RoutingActivationType
from uds.transport.ethernet.enum.routing_activation_response_code import RoutingActivationResponseCode
from uds.transport.ethernet.message import DoIPMessage

class RoutingActivationRequest(DoIPMessage):
    """
    Routing activation is required to route diagnostic message from tester to ECU.
    ECU will tells to tester if routing is required or not regarding state machine implemented
    in the ECU.

    Some events can require tester to request a new routing activation otherwise ECU won't process
    any subsequents diagnostic message.

    See ISO 13400 for more information.
    """
    _pack_   =  1
    _fields_ =  [
                    ("source_address", c_uint16), # Source address to register on ECU (logical)
                    ("activation_type", c_uint8),
                    ("reserved", 4 * c_uint8), # ISO reserved
                ]

    CONNECTION_KIND = ConnectionKind.TCP
    PAYLOAD_TYPE    = DoIPPayloadType.ROUTING_ACTIVATION_REQUEST
    
    def __init__(self, source_address = 0x0E00, activation_type = RoutingActivationType.DEFAULT):
        super(RoutingActivationRequest, self).__init__()
        self.source_address  = source_address
        self.activation_type = activation_type

    def __bytes__(self):
        """
        Bytes representation of the final DoIP Message.

        DoIPHeader / Payload / OEM_SPECIFIC (if there's one) should all being concatenated.
        """
        b = bytearray(self) # Hack to avoid recursive call to __bytes__()

        return bytes(b)

    def __repr__(self):
        s = """{}\rPayload:
                 \r\tSource address : {}
                 \r\tActivation type : {}
                 \r\tISO Reserved : 0x{}
            """.format  (
                            super(RoutingActivationRequest, self).__repr__(),
                            hex(self.source_address),
                            RoutingActivationType(self.activation_type).name,
                            "".join([hex(b)[2:] for b in self.reserved]), # Convert 4 * c_ubyte to hex value
                        )

        return s

class RoutingActivationResponse(DoIPMessage):
    """
    Response to a routing activation request.

    Response is containing two important information:
        - Logical address tester (target address on the bus related to the ECU answering)
        - Response code (indicates if routing has been done successfully or if something is not fitting with requirements)
    """
    _pack_      =   1
    _fields_    =   [
                        ("logical_address_tester", c_uint16), # Should be source address used with request
                        ("logical_address_ecu", c_uint16), # Logical address of the ECU (virtual address)
                        ("response_code", c_uint8),
                        ("reserved", 4 * c_uint8), # ISO reserved
                    ]

    CONNECTION_KIND = ConnectionKind.TCP
    PAYLOAD_TYPE    = DoIPPayloadType.ROUTING_ACTIVATION_RESPONSE

    def __init__(self):
        super(RoutingActivationResponse, self).__init__()

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tLogical address tester: {}
                    \r\tLogical address ECU: {}
                    \r\tResponse code: {}
                    \r\tOEM specific: {}
            """.format  (
                            super(RoutingActivationResponse, self).__repr__(),
                            hex(self.logical_address_tester),
                            hex(self.logical_address_ecu),
                            RoutingActivationResponseCode(self.response_code).name,
                        )       

        return s