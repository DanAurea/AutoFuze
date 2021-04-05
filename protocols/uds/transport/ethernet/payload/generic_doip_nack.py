from ctypes import c_uint8

from uds.transport.ethernet.enum.generic_nack import GenericNACKEnum
from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class GenericNACK(DoIPMessage):
    """
    Generic DoIP NACK (coming out of ECU)
    """
    _pack_   =  1
    _fields_ =  [
                    ("nack_code", c_uint8)
                ]

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tNACK code: {}
            """.format  (
                            super(GenericDoIPNack, self).__repr__(),
                            GenericNACKEnum(self.nack_code).name,
                        )

        return s