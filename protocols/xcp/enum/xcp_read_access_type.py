from enum import IntEnum

class XcpReadAccessType(IntEnum):
    """
    This class describes an ecu access type.
    """
    XCP_READ_ACCESS_NOT_ALLOWED      = 0x00
    XCP_READ_ACCESS_WITHOUT_ECU_ONLY = 0x01
    XCP_READ_ACCESS_WITH_ECU_ONLY    = 0x02
    XCP_READ_ACCESS_DONT_CARE        = 0x03