from enum import IntEnum

class DiagnosticPowerMode(IntEnum):
    """
    This class enumerates all generic doip NACK.
    """
    NOT_READY      = 0X00
    READY          = 0X01
    NOT_SUPPORTED  = 0X02
    # ISO_RESERVED = 0X03
    # ISO_RESERVED = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__diagnostic_power_mode__ = [(t.name, t.value) for t in DiagnosticPowerMode]

__diagnostic_power_mode__ = dict(    
                                    __diagnostic_power_mode__ + 
                                    [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x03, 0x100)]
                                )

# Override diagnostic power modes with missing field
DiagnosticPowerMode = IntEnum("DiagnosticPowerMode", __diagnostic_power_mode__)