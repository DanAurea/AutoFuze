from enum import IntEnum

class GranularityOdtEntrySizeDaq(IntEnum):
    """
    This class describes an identification field type.
    """
    GRANULARITY_ODT_ENTRY_SIZE_DAQ_BYTE  = 0x01
    GRANULARITY_ODT_ENTRY_SIZE_DAQ_WORD  = 0x02
    GRANULARITY_ODT_ENTRY_SIZE_DAQ_DWORD = 0x04
    GRANULARITY_ODT_ENTRY_SIZE_DAQ_DLONG = 0x08