from enum import IntEnum

class DiagnosticMessageNACKEnum(IntEnum):
    """
    This class enumerates all diagnostic message NACK in DoIP.
    """
    # ISO_RESERVED               = 0X00
    # ISO_RESERVED               = 0X01
    INVALID_SOURCE_ADDRESS       = 0X02
    UNKNOWN_TARGET_ADDRESS       = 0X03
    DIAGNOSTIC_MESSAGE_TOO_LARGE = 0X04
    OUT_OF_MEMORY                = 0X05
    TARGET_UNREACHABLE           = 0X06
    UNKNOWN_NETWORK              = 0X07
    TRANSPORT_PROTOCOL_ERROR     = 0X08
    # ISO_RESERVED               = 0X09
    # ISO_RESERVED               = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__diagnostic_message_nack__ = [(t.name, t.value) for t in DiagnosticMessageNACKEnum]

__diagnostic_message_nack__ = dict(    
                                    __diagnostic_message_nack__ + 
                                    [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x00, 0x02)] +
                                    [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x09, 0x100)]
                                )

# Override diagnostic message nack with missing field
DiagnosticMessageNACKEnum = IntEnum("DiagnosticMessageNACKEnum", __diagnostic_message_nack__)