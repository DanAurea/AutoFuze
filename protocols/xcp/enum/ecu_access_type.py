from enum import IntEnum

class EcuAccessType(IntEnum):
    """
    This class describes an ecu access type.
    """
    ECU_ACCESS_NOT_ALLOWED      = 0x00
    ECU_ACCESS_WITHOUT_XCP_ONLY = 0x01
    ECU_ACCESS_WITH_XCP_ONLY    = 0x02
    ECU_ACCESS_DONT_CARE        = 0x03