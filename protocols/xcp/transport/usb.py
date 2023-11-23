from ctypes import LittleEndianStructure, c_uint8

from xcp.transport.base import TransportBase
from struct import pack

class UsbHeader(LittleEndianStructure):
    """
    This class describes a USB header.
    USB composition vary regarding XCP packet:
    
        Packet length can be either a byte or a word.
        Control CTR is always the same size as packet length.
    """

    _pack_   = 1
    _fields_ =  [
                    ("_packet_len", c_uint8),
                    ("_control_ctr", c_uint8),
                ]

    def __init__(self, packet_len = 0x00, control_ctr = 0x00):
        self._packet_len  = packet_len
        self._control_ctr = control_ctr

    def update_control(self):
        """
        Increment control counter for flow control of Ethernet traffic.
        """

        # TODO: Handle overflow if control ctr goes over 0xFF
        self._control_ctr += 0x01

class UsbTail(LittleEndianStructure):

    def __init__(self):
        self._fill = 0x00

    def __bytes__(self):
        """
        Return bytes representation of USB tail.
        """
        # Content is irrelevant so we "don't care"
        return bytes(bytearray(self._fill))

class UsbTransport(TransportBase):
    """
    This class describes Universal Serial Bus (USB) transport layer used for XCP.
    XCP on USB is adding an extra header and tail to XCP frame.
    """
    def __init__(self):
        super(UsbTransport, self).__init__()
        self._header = UsbHeader()
        self._tail   = UsbTail()

    def create_message(self, packet):
        """
        Creates a XCP USB frame 

        :param      packet:  The packet to send.
        :type       packet:  XCPPacketBase
        
        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        
        frame_bytes = super(UsbTransport, self).create_message(packet)
        self._header.update_control()

        return bytes(frame_bytes)