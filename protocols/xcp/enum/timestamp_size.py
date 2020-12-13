from enum import IntEnum

class TimestampSize(IntEnum):
    """
    This class describes a timestamp size.
    """
    NO_TIME_STAMP = 0x00
    SIZE_BYTE     = 0x01
    SIZE_WORD     = 0x02
    SIZE_DWORD    = 0x04