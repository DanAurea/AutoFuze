from enum import IntEnum

class FurtherActionRequired(IntEnum):
    """
    This class enumerates all further actions required when routing activation is requested.
    """
    NO_FURTHER_ACTION_REQUIRED  = 0X00
    # ISO_RESERVED              = 0X01
    # ISO_RESERVED              = 0X0F
    ROUTING_ACTIVATION_REQUIRED = 0X10
    # OEM_SPECIFIC_USE          = 0X11
    # OEM_SPECIFIC_USE          = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__further_action_required__ = [(t.name, t.value) for t in FurtherActionRequired]

__further_action_required__ =   dict(    
                                        __further_action_required__ + 
                                        [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x01, 0x10)] +
                                        [("OEM_SPECIFIC_" + hex(t).upper(), t) for t in range(0x11, 0x100)]
                                    )

# Override further action required with missing field
FurtherActionRequired = IntEnum("FurtherActionRequired", __further_action_required__)