from enum import IntEnum

class VINGIDSyncStatus(IntEnum):
    """
    This class enumerates all VIN/GID sync status.
    """
    VIN_GID_SYNCHRONIZED     = 0X00
    # ISO_RESERVED           = 0X01
    # ISO_RESERVED           = 0X0F
    VIN_GID_NOT_SYNCHRONIZED = 0X10
    # ISO_RESERVED           = 0X11
    # ISO_RESERVED           = 0XFF