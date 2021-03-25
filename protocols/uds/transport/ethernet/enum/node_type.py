from enum import IntEnum

class NodeType(IntEnum):
    """
    This class enumerates all doip node types.
    """
    DOIP_GATEWAY   = 0X00
    DOIP_NODE      = 0X01
    # ISO_RESERVED = 0X02
    # ISO_RESERVED = 0XFF