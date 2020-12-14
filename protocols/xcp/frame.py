class XcpFrame(object):
    """
    This class describes a xcp frame as XCP V1.0 standard state.
    A XCP frame is containing:
        1. XCP Header
            - Header is dependent on transport layer
        2. XCP Packet
            - Packet is a generic part of the protocol and is independent from the transport layer used.
        3. XCP Tail
            - Tail is dependent on transport layer
    """

    def __init__(self, header = None, packet = None, tail = None):
        self.header = header
        self.packet = packet
        self.tail   = tail

    def __bytes__(self):
        frame_bytes = bytearray()

        try:
            frame_bytes.extend(bytes(self.header))     
        except:
            pass
        
        try:
            frame_bytes.extend(bytes(self.packet))     
        except:
            pass

        try:
            frame_bytes.extend(bytes(self.tail))     
        except:
            pass

        return bytes(frame_bytes)