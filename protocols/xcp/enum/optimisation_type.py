from enum import IntEnum

class OptimisationType(IntEnum):
    """
    This class describes an optimisation type.
    """
    OPTIMISATION_TYPE_DEFAULT            = 0x00
    OPTIMISATION_TYPE_ODT_TYPE_16        = 0x01
    OPTIMISATION_TYPE_ODT_TYPE_32        = 0x02
    OPTIMISATION_TYPE_ODT_TYPE_64        = 0x03
    OPTIMISATION_TYPE_ODT_TYPE_ALIGNMENT = 0x04
    OPTIMISATION_TYPE_MAX_ENTRY_SIZE     = 0x05