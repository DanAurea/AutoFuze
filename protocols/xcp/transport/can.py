from ctypes import LittleEndianStructure, c_uint8
from xcp.transport.base import XCPTransportBase

class CanFrame(LittleEndianStructure):
    _pack_   = 1
    _fields_ =  [
                    ('dlc', c_uint8)
                ]

class CanTail(LittleEndianStructure):
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

class CanTransport(XCPTransportBase):
    """
    This class describes Controller Area Network (CAN) transport layer used for XCP.
    XCP on CAN is adding an extra tail to XCP frame.
    No header is added.
    """
    MAX_DLC = 8 # Max data length code of CAN protocol

    def __init__(self, max_dlc_required = False, fill = False):
        self._max_dlc_required = max_dlc_required
        self._fill             = fill
        self._tail             = CanTail()

    def __bytes__(self):
        """
        Creates a XCP CAN frame 

        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        pdu_len = len(bytes(self._pdu))

        if self._max_dlc_required or self._fill:
            dlc = self.MAX_DLC
        else:
            # TODO : Refactor to handle overflow
            dlc = min(self.MAX_DLC, pdu_len)

        # Fill tail with empty bytes to reach MAX_DLC
        if self._fill and pdu_len < self.MAX_DLC:
            self._tail.fill = self.MAX_DLC - pdu_len

        frame = CanFrame()
        frame.dlc = dlc

        return bytes(frame) + super(CanTransport, self).__bytes__()