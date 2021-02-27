from enum import IntEnum

class RoutingActivationType(IntEnum):
    """
    This class enumerates all routing activation types.
    """
    DEFAULT          = 0X00
    WWH_OBD          = 0X01
    ISO_RESERVED     = 0X02
    ISO_RESERVED     = 0XDF
    CENTRAL_SECURITY = 0XE0
    OEM_SPECIFIC_USE = 0XE1
    OEM_SPECIFIC_USE = 0XFF