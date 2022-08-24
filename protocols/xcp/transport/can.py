from ctypes import BigEndianStructure
from struct import pack
from xcp.transport.base import TransportBase

class CanTail(BigEndianStructure):
    """
    This class describes a Controller Area Network (CAN) tail.
    Tail composition vary regarding XCP packet length and 
    Data Length code (DLC) of CAN frame:

        - XCP packet length == MAX_DLC == 8
            . Tail is empty
        - XCP packet length < 8
            . Either DLC is set to XCP packet length and tail is empty
            . Either DLC is set to MAX_DLC and tail is filled with extra data

    Slave can inform Master with MAX_DLC_REQUIRED that every frame should be
    defined as 8 bytes.
    """
    def __init__(self):
        self._fill = 0x0

    def _set_fill(self, fill):
        self._fill = fill

    def __bytes__(self):
        """
        Return bytes representation of CAN Tail.
        """
        # Content is irrelevant so we "don't care"
        return bytes(bytearray(self._fill))

    # Create a setter for fill parameter (Write only member)
    fill = property(fset = _set_fill)

    del _set_fill

class CanTransport(TransportBase):
    """
    This class describes Controller Area Network (CAN) transport layer used for XCP.
    XCP on CAN is adding an extra tail to XCP frame.
    No header is added.
    """
    MAX_DLC = 8 # Max data length code of CAN protocol

    def __init__(self, max_dlc_required = False, should_fill = False):
        super(CanTransport, self).__init__()
        self._max_dlc_required = max_dlc_required
        self._should_fill      = should_fill
        self._tail             = CanTail()

    def create_message(self, packet):
        """
        Creates a XCP CAN frame 

        :param      packet:  The packet to send.
        :type       packet:  XCPPacketBase
        
        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        frame_bytes = bytearray()

        packet_len = len(bytes(packet))

        if self._max_dlc_required or self._should_fill:
            dlc = self.MAX_DLC
        else:
            dlc = packet_len

        # Fill tail with empty bytes to reach MAX_DLC
        if self._should_fill and packet_len < self.MAX_DLC:
            self._tail.fill = self.MAX_DLC - packet_len

        frame_bytes.extend(pack("<B", dlc))
        frame_bytes.extend(super(CanTransport, self).create_message(packet))

        return bytes(frame_bytes)