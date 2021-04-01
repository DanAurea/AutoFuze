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
                    ("_protocol_version", c_uint8),
                    ("_inverse_protocol_version", c_uint8),
                    ("_payload_type", c_uint16),
                    ("_payload_length", c_uint32),
                    #("payload", x * c_byte) Payload content
                ]

    def __init__(self, protocol_version = DoIPProtocolVersion.ISO_13400_2_2012, inverse_protocol_version = 0xFF - DoIPProtocolVersion.ISO_13400_2_2012, payload_type = DoIPPayloadType.GENERIC_DOIP_HEADER_NEGATIVE_ACK, payload = None):
        self._protocol_version         = DoIPProtocolVersion(protocol_version)
        self._inverse_protocol_version = inverse_protocol_version
        self._payload_type             = DoIPPayloadType(payload_type)
        self._payload_length           = 0

        # TODO: Do not mixin payload/pdu (proper to diagnostic message) furthermore payload should be automatically set by subclassing
        # this will allow to update automatically payload length
        self.payload                   = payload

    @property
    def payload(self):
        """
        Payload getter
        
        :returns:   Payload
        :rtype:     DoIPMessage
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Payload setter, update automatically payload length in header.
        
        :param      payload:  The payload
        :type       payload:  { type_description }
        """
        self._payload        = payload

        if self._payload:
            self._payload_length = len(bytes(self._payload))

    def __repr__(self):
        header =    """DoIP Header:\
                        \r\t Protocol version: {} 
                        \r\t Inverse protocol version: {} 
                        \r\t Payload type: {} 
                        \r\t Payload length: {} bytes
                    """.format  (
                                    DoIPProtocolVersion(self._protocol_version).name, # Mandatory because ctypes and instance member are mixing together
                                    hex(self._inverse_protocol_version & 0xFF),
                                    DoIPPayloadType(self._payload_type).name, # Mandatory because ctypes and instance member are mixing together
                                    str(self._payload_length)
                                )

        return header