from enum import IntEnum

class IdentificationFieldType(IntEnum):
    """
    This class describes an identification field type.
    """
    IDENTIFICATION_FIELD_TYPE_ABSOLUTE              = 0x00
    IDENTIFICATION_FIELD_TYPE_RELATIVE_BYTE         = 0x01
    IDENTIFICATION_FIELD_TYPE_RELATIVE_WORD         = 0x02
    IDENTIFICATION_FIELD_TYPE_RELATIVE_WORD_ALIGNED = 0x03