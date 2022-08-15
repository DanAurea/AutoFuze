from enum import IntFlag

class ConnectionKind(IntFlag):
    """
    Set int flag for connection types used with Ethernet.
    """
    TCP = 1
    UDP = 2