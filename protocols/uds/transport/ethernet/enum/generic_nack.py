from enum import IntEnum

class GenericNACKEnum(IntEnum):
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

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__generic_nack__ = [(t.name, t.value) for t in GenericNACKEnum]

__generic_nack__ = dict(    
                            __generic_nack__ + 
                            [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x05, 0x100)]
                        )

# Override generic nack with missing field
GenericNACKEnum = IntEnum("GenericNACKEnum", __generic_nack__)