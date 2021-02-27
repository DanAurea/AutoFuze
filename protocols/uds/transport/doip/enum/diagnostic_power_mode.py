from enum import IntEnum

class DiagnosticPowerMode(IntEnum):
    """
    This class enumerates all generic doip NACK.
    """
    NOT_READY      = 0X00
    READY          = 0X01
    NOT_SUPPORTED  = 0X02
    # ISO_RESERVED = 0X03
    # ISO_RESERVED = 0XFF