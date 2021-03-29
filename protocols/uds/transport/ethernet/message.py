from ctypes import BigEndianStructure, c_uint8, c_uint16, c_uint32

from uds.transport.ethernet.enum.protocol_version import DoIPProtocolVersion
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class DoIPMessage(BigEndianStructure):
    """
    This class describes a DoIP message.

    ISO 13400 defines the header as following:
        - protocol_version : DoIP version (1 byte)
        - inverse_protocol_version: 0xFF - protocol_version (1 byte)
        - payload_type: Payload type ID (2 bytes)
        - payload_length: Payload length excluding this header (4 bytes)

    Any class requiring to communicate over UDS on Ethernet should subclass this one.
    Subclassing will automatically add the required DoIP header.
    """
    _pack_   = 1
    _fields_ =  [
                    ("protocol_version", c_uint8),
                    ("inverse_protocol_version", c_uint8),
                    ("payload_type", c_uint16),
                    ("payload_length", c_uint32),
                    #("payload", x * c_byte) Payload content
                ]

    def __init__(self, protocol_version = DoIPProtocolVersion.ISO_13400_2_2012, inverse_protocol_version = 0xFF - DoIPProtocolVersion.ISO_13400_2_2012, payload_type = DoIPPayloadType.GENERIC_DOIP_HEADER_NEGATIVE_ACK, payload_length = 8):
        self.protocol_version         = protocol_version
        self.inverse_protocol_version = inverse_protocol_version
        self.payload_type             = payload_type
        self.payload_length           = payload_length

    def __repr__(self):
        header =    """\rDoIP Header:\
                        \r\t Protocol version: {} 
                        \r\t Inverse protocol version: {} 
                        \r\t Payload type: {} 
                        \r\t Payload length: {} bytes
                    """.format  (
                                    str(DoIPProtocolVersion(self.protocol_version)),
                                    hex(self.inverse_protocol_version & 0xFF),
                                    str(DoIPPayloadType(self.payload_type)),
                                    str(self.payload_length)
                                )

        return header 