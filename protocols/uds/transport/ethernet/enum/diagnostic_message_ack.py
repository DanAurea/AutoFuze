from enum import IntEnum

class DiagnosticMessageACKEnum(IntEnum):
    """
    This class enumerates all diagnostic message NACK in DoIP.
    """
    CORRECTLY_RECEIVED = 0X00
    # ISO_RESERVED     = 0X01
    # ISO_RESERVED     = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__diagnostic_message_ack__ = [(t.name, t.value) for t in DiagnosticMessageACKEnum]

__diagnostic_message_ack__ = dict(    
                                    __diagnostic_message_ack__ + 
                                    [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x01, 0x100)]
                                )

# Override diagnostic message ack with missing field
DiagnosticMessageACKEnum = IntEnum("DiagnosticMessageACKEnum", __diagnostic_message_ack__)