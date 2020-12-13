from enum import IntEnum

class OverloadIndication(IntEnum):
    """
    This class describes an overload indication.
    """
    NO_OVERLOAD_INDICATION    = 0x00
    OVERLOAD_INDICATION_PID   = 0x01
    OVERLOAD_INDICATION_EVENT = 0x02