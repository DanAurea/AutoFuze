from enum import IntEnum

class ChecksumType(IntEnum):
    """
    This class describes a checksum type.
    """
    XCP_USER_DEFINED = 0xFF
    
    XCP_CRC_32       = 0x09
    XCP_CRC_16_CITT  = 0x08
    XCP_CRC_16       = 0x07
    
    XCP_ADD_44       = 0x06
    XCP_ADD_24       = 0x05
    XCP_ADD_22       = 0x04
    XCP_ADD_14       = 0x03
    XCP_ADD_12       = 0x02
    XCP_ADD_11       = 0x01