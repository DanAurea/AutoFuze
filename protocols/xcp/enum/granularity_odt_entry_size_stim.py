from enum import IntEnum

class GranularityOdtEntrySizeStim(IntEnum):
    """
    This class describes an identification field type.
    """
    GRANULARITY_ODT_ENTRY_SIZE_STIM_BYTE  = 0x01
    GRANULARITY_ODT_ENTRY_SIZE_STIM_WORD  = 0x02
    GRANULARITY_ODT_ENTRY_SIZE_STIM_DWORD = 0x04
    GRANULARITY_ODT_ENTRY_SIZE_STIM_DLONG = 0x08