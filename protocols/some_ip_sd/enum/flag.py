from enum import IntFlag

class SOMEIPSDFlag(IntFlag):
    REBOOT_FLAG           = 0x80
    UNICAST_FLAG          = 0x40
    EXPLICIT_INITIAL_DATA = 0x20