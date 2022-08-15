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

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__vin_gid_sync_status__ = [(t.name, t.value) for t in VINGIDSyncStatus]

__vin_gid_sync_status__ =   dict(    
                                    __vin_gid_sync_status__ + 
                                    [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x01, 0x10)] +
                                    [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x11, 0x100)]
                                )

# Override vin gid sync status with missing field
VINGIDSyncStatus = IntEnum("VINGIDSyncStatus", __vin_gid_sync_status__)