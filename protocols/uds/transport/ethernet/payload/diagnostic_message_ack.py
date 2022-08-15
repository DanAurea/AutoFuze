from ctypes import c_uint8, c_uint16

from uds.transport.ethernet.enum.connection_kind import ConnectionKind
from uds.transport.ethernet.enum.diagnostic_message_ack import DiagnosticMessageACKEnum
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.message import DoIPMessage

class DiagnosticMessageACK(DoIPMessage):
    """
    Diagnostic message acknowledgement, sent when a diagnostic message has been
    correctly processed by the ECU.
    """
    _pack_   = 1
    _fields_ =  [
                    ("source_address", c_uint16),
                    ("target_address", c_uint16),
                    ("ack_code", c_uint8),
                    #("previous_message", c_byte * _payload_length)
                ]
    
    CONNECTION_KIND = ConnectionKind.TCP
    PAYLOAD_TYPE    = DoIPPayloadType.DIAGNOSTIC_MESSAGE_POSITIVE_ACK
    
    def __init__(self):
        super(DiagnosticMessageACK, self).__init__()

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tSource address: {}
                    \r\tTarget address: {}
                    \r\tACK code: {}
            """.format  (
                            super(DiagnosticMessageACK, self).__repr__(),
                            hex(self.source_address),
                            hex(self.target_address),
                            DiagnosticMessageACKEnum(self.ack_code).name,
                        )

        # TODO: Handle previous message decoding (check how to do it properly)

        return s