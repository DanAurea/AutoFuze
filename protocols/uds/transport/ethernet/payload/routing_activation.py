from ctypes import c_char, c_uint8, c_uint16

from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.enum.routing_activation_type import RoutingActivationType

class RoutingActivationRequest(DoIPMessage):
    _pack_ = 1
    _fields_ =  [
                    ("source_address", c_uint16), # Source address to register on ECU (logical)
                    ("activation_type", c_uint8),
                    ("reserved", 4 * c_uint8), # ISO reserved
                    ("oem_specific", 4 * c_uint8) # Optional
                ]

    def __init__(self, source_address = 0x0000, activation_type = RoutingActivationType.DEFAULT):
        super(RoutingActivationRequest, self).__init__(payload_type = DoIPPayloadType.ROUTING_ACTIVATION_REQUEST)
        self.source_address  = source_address
        self.activation_type = activation_type

    def __repr__(self):
        s = """{}\rPayload:
                 \r\tSource address : {}
                 \r\tActivation type : {}
                 \r\tISO Reserved : 0x{}
                 \r\tOEM specific : 0x{}
            """.format  (
                            super(RoutingActivationRequest, self).__repr__(),
                            hex(self.source_address),
                            RoutingActivationType(self.activation_type).name,
                            "".join([hex(b)[2:] for b in self.reserved]), # Convert 4 * c_ubyte to hex value
                            "".join([hex(b)[2:] for b in self.oem_specific]), # Convert 4 * c_ubyte to hex value
                        )

        return s

class RoutingActivationResponse(object):
    pass