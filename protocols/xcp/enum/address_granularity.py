from enum import IntEnum

class AddressGranularity(IntEnum):
    """
    This class describes an address granularity.
    """
    ADDRESS_GRANULARITY_BYTE  = 0x01
    ADDRESS_GRANULARITY_WORD  = 0x02
    ADDRESS_GRANULARITY_DWORD = 0x04