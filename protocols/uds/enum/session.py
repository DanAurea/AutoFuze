from enum import IntEnum

class Session(IntEnum):
    DEFAULT_SESSION                  = 0x01
    PROGRAMMING_SESSION              = 0x02
    EXTENDED_DIAGNOSTIC_SESSION      = 0x03
    SAFETY_SYSTEM_DIAGNOSTIC_SESSION = 0x04
    # OEM SPECIFIC SESSION >= 0x05

# TODO: Check if there's not another way to handle such requirement. It would be better to allow user to add member itself.
# Hack: Not intended to be imported but required to define missing fields in a safe manner
__session__ = [(t.name, t.value) for t in Session]

__session__ =   dict(    
                        __session__ + 
                        [("OEM_SPECIFIC_" + hex(t).upper(), t) for t in range(0x05, 0x100)]
                    )

# Override session with missing field
Session = IntEnum("Session", __session__)