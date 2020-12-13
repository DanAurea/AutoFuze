from enum import IntFlag
from xcp.enum.parameter_bit import TimestampModeBit

class TimestampUnit(IntFlag):
    """
    This class describes a timestamp unit.
    """
    DAQ_TIMESTAMP_UNIT_1NS   = 0x00
    DAQ_TIMESTAMP_UNIT_10NS  = TimestampModeBit.UNIT_0
    DAQ_TIMESTAMP_UNIT_100NS = TimestampModeBit.UNIT_1
    DAQ_TIMESTAMP_UNIT_1US   = TimestampModeBit.UNIT_0 | TimestampModeBit.UNIT_1
    DAQ_TIMESTAMP_UNIT_10US  = TimestampModeBit.UNIT_2
    DAQ_TIMESTAMP_UNIT_100US = TimestampModeBit.UNIT_0 | TimestampModeBit.UNIT_2
    DAQ_TIMESTAMP_UNIT_1MS   = TimestampModeBit.UNIT_1 | TimestampModeBit.UNIT_2
    DAQ_TIMESTAMP_UNIT_10MS  = TimestampModeBit.UNIT_0 | TimestampModeBit.UNIT_1 | TimestampModeBit.UNIT_2
    DAQ_TIMESTAMP_UNIT_100MS = TimestampModeBit.UNIT_3
    DAQ_TIMESTAMP_UNIT_1S    = TimestampModeBit.UNIT_0 | TimestampModeBit.UNIT_3