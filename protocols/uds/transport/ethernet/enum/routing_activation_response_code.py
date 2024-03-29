from enum import IntEnum

class RoutingActivationResponseCode(IntEnum):
    """
    This class enumerates all routing activation response code.
    """
    UNKNOWN_SOURCE_ADDRESS                               = 0X00
    ALL_TCP_DATA_ARE_REGISTERED_AND_ACTIVE               = 0X01
    SOURCE_ADDRESS_NOT_FIT_ACTIVATED_SOCKET              = 0X02
    SOURCE_ADDRESS_REGISTERED_AND_ACTIVE_ON_OTHER_SOCKET = 0X03
    MISSING_AUTHENTICATION                               = 0X04
    REJECTED_CONFIRMATION                                = 0X05
    UNSUPPORTED_ACTIVATION_TYPE                          = 0X06
    # ISO_RESERVED                                       = 0X07
    # ISO_RESERVED                                       = 0X0F
    ROUTING_SUCCESFULLY_ACTIVATED                        = 0X10
    ROUTING_REQUIRE_CONFIRMATION                         = 0X11
    # ISO_RESERVED                                       = 0X12
    # ISO_RESERVED                                       = 0XDF
    # VEHICLE_MANUFACTURER_SPECIFIC                      = 0XE0
    # VEHICLE_MANUFACTURER_SPECIFIC                      = 0XFE
    # ISO_RESERVED                                       = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__routing_activation_response_code__ = [(t.name, t.value) for t in RoutingActivationResponseCode]

__routing_activation_response_code__ = dict(    
                                                __routing_activation_response_code__ + 
                                                [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x07, 0x10)] + 
                                                [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x12, 0xE0)] + 
                                                [("OEM_SPECIFIC_" + hex(t).upper(), t) for t in range(0xE0, 0xFF)] +
                                                [("ISO_RESERVED_0xFF", 0xFF)]
                                            )

# Override routing activation response codes with missing field
RoutingActivationResponseCode = IntEnum("RoutingActivationResponseCode", __routing_activation_response_code__)