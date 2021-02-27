from enum import IntEnum

class FurtherActionRequired(IntEnum):
    """
    This class enumerates all further actions required when routing activation is requested.
    """
    NO_FURTHER_ACTION_REQUIRED  = 0X00
    # ISO_RESERVED              = 0X01
    # ISO_RESERVED              = 0X0F
    ROUTING_ACTIVATION_REQUIRED = 0X10
    # OEM_SPECIFIC_USE          = 0X11
    # OEM_SPECIFIC_USE          = 0XFF