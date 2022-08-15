from enum import IntEnum

class DoIPProtocolVersion(IntEnum):
    """
    This class enumerates all DoIP protocol version.
    """
    ISO_13400_2_2010 = 0X01
    ISO_13400_2_2012 = 0X02
    # ISO_RESERVED   = 0X03
    # ISO_RESERVED   = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__doip_protocol_version__ = [(t.name, t.value) for t in DoIPProtocolVersion]

__doip_protocol_version__ = dict(    
                                    __doip_protocol_version__ + 
                                    [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x03, 0x100)]
                                )

# Override doip protocol version with missing field
DoIPProtocolVersion = IntEnum("DoIPProtocolVersion", __doip_protocol_version__)