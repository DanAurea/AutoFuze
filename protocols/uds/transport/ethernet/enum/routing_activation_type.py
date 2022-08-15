from enum import IntEnum

class RoutingActivationType(IntEnum):
    """
    This class enumerates all routing activation types.
    """
    DEFAULT          = 0X00
    WWH_OBD          = 0X01
    #ISO_RESERVED     = 0X02
    #ISO_RESERVED     = 0XDF
    CENTRAL_SECURITY = 0XE0
    #OEM_SPECIFIC_USE = 0XE1
    #OEM_SPECIFIC_USE = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__routing_activation_types__ = [(t.name, t.value) for t in RoutingActivationType]

__routing_activation_types__ = dict(    
                                        __routing_activation_types__ + 
                                        [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x02, 0xE0)] +
                                        [("OEM_SPECIFIC_" + hex(t).upper(), t) for t in range(0xE1, 0x100)]
                                    )

# Override routing activation types with missing field
RoutingActivationType = IntEnum("RoutingActivationType", __routing_activation_types__)