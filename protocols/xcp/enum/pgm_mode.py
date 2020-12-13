from enum import IntEnum

class PgmMode(IntEnum):
    """
    This class describes a program mode.
    """
    PGM_MODE_ABSOLUTE                = 0x01
    PGM_MODE_FUNCTIONAL              = 0x02
    PGM_MODE_ABSOLUTE_AND_FUNCTIONAL = 0x03