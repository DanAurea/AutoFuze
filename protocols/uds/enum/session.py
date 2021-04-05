from enum import IntEnum

class Session(IntEnum):
    DEFAULT_SESSION                  = 0x01
    PROGRAMMING_SESSION              = 0x02
    EXTENDED_DIAGNOSTIC_SESSION      = 0x03
    SAFETY_SYSTEM_DIAGNOSTIC_SESSION = 0x04
    # OEM SPECIFIC SESSION >= 0x05