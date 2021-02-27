from enum import IntEnum

class GenericNACK(IntEnum):
    """
    This class enumerates all generic doip NACK.
    """
    INCORRECT_PATTERN_FORMAT = 0X00
    UNKNOWN_PAYLOAD_TYPE     = 0X01
    MESSAGE_TOO_LARGE        = 0X02
    OUT_OF_MEMORY            = 0X03
    INVALID_PAYLOAD_LENGTH   = 0X04
    # ISO_RESERVED           = 0X05
    # ISO_RESERVED           = 0XFF