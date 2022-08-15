from ctypes import c_uint8

from uds.transport.ethernet.enum.connection_kind import ConnectionKind
from uds.transport.ethernet.enum.generic_nack import GenericNACKEnum
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.message import DoIPMessage

class GenericNACK(DoIPMessage):
    """
    Generic DoIP NACK (coming out of ECU)
    """
    _pack_   =  1
    _fields_ =  [
                    ("nack_code", c_uint8)
                ]

    CONNECTION_KIND = ConnectionKind.TCP | ConnectionKind.UDP
    PAYLOAD_TYPE    = DoIPPayloadType.GENERIC_DOIP_HEADER_NEGATIVE_ACK

    def __init__(self):
        super(GenericNACKEnum, self).__init__()

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tNACK code: {}
            """.format  (
                            super(GenericDoIPNack, self).__repr__(),
                            GenericNACKEnum(self.nack_code).name,
                        )

        return s