from enum import IntEnum

class DaqListType(IntEnum):
    """
    This class describes a daq list type.
    """
    DAQ      = 0x01
    STIM     = 0x02
    DAQ_STIM = 0x03