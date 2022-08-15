from enum import IntEnum

class NodeType(IntEnum):
    """
    This class enumerates all doip node types.
    """
    DOIP_GATEWAY   = 0X00
    DOIP_NODE      = 0X01
    # ISO_RESERVED = 0X02
    # ISO_RESERVED = 0XFF

# Hack: Not intended to be imported but required to define missing fields in a safe manner
__node_type__ = [(t.name, t.value) for t in NodeType]

__node_type__ = dict(    
                        __node_type__ + 
                        [("ISO_RESERVED_" + hex(t).upper(), t) for t in range(0x02, 0x100)]
                    )

# Override node type with missing field
NodeType = IntEnum("NodeType", __node_type__)