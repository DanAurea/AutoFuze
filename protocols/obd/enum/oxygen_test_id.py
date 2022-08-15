from enum import IntEnum

class OxygenTestID(IntEnum):
    RICH_LEAN_VOLTAGE_THRES = 0x01
    LEAN_RICH_VOLTAGE_THRES = 0x02
    LOW_VOLTAGE             = 0x03
    HIGH_VOLTAGE            = 0x04
    RCH_LEAN_SWITCH_TIME    = 0x05