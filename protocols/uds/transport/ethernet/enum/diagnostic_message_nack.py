from enum import IntEnum

class DiagnosticMessageNACK(IntEnum):
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