from ctypes import c_uint8, c_uint16

from uds.transport.ethernet.enum.diagnostic_message_nack import DiagnosticMessageNACKEnum
from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class DiagnosticMessageNACK(DoIPMessage):
    """
    Diagnostic message negative acknowledgement, sent when a diagnostic message hasn't been
    correctly processed by the ECU.

    Reason can be found in diagnostic_message_nack.py.
    """
    _pack_   = 1
    _fields_ =  [
                    ("source_address", c_uint16),
                    ("target_address", c_uint16),
                    ("nack_code", c_uint8),
                    #("previous_message", c_byte * _payload_length)
                ]
    
    def __init__(self):
        super(DiagnosticMessageNACK, self).__init__(payload_type = DoIPPayloadType.DIAGNOSTIC_MESSAGE_NEGATIVE_ACK)

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tSource address: {}
                    \r\tTarget address: {}
                    \r\tNACK code: {}
            """.format  (
                            super(DiagnosticMessageNACK, self).__repr__(),
                            hex(self.source_address),
                            hex(self.target_address),
                            DiagnosticMessageNACKEnum(self.nack_code).name,
                        )

        # TODO: Handle previous message decoding (check how to do it properly)

        return s