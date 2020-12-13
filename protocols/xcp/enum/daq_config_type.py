from enum import IntEnum

class DaqConfigType(IntEnum):
    """
    This class describes a daq configuration type.
    """
    STATIC  = 0x00
    DYNAMIC = 0x01