from enum import IntEnum

class DiagnosticMessageACKEnum(IntEnum):
    """
    This class enumerates all diagnostic message NACK in DoIP.
    """
    CORRECTLY_RECEIVED = 0X00
    # ISO_RESERVED     = 0X01
    # ISO_RESERVED     = 0XFF