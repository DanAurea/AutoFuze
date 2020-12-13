from enum import IntEnum

class XcpWriteAccessType(IntEnum):
    """
    This class describes an ecu access type.
    """
    XCP_WRITE_ACCESS_NOT_ALLOWED      = 0x00
    XCP_WRITE_ACCESS_WITHOUT_ECU_ONLY = 0x01
    XCP_WRITE_ACCESS_WITH_ECU_ONLY    = 0x02
    XCP_WRITE_ACCESS_DONT_CARE        = 0x03