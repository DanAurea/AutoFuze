from enum import IntEnum

class ByteOrder(IntEnum):
    """
    This class describes a byte order.
    """
    BYTE_ORDER_MSB_LAST  = 0x00
    BYTE_ORDER_MSB_FIRST = 0x01