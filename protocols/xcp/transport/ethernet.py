from ctypes import BigEndianStructure, c_uint16

from xcp.transport.base import TransportBase
from struct import pack

class XcpEthernetHeader(BigEndianStructure):
    """
    This class describes a XCP ethernet header.
    XCP Ethernet header is composed as:
        - 2 bytes describing XCP Packet Length
        - 2 bytes describing a control ctr (used to detect missing packets in flow control)
    """

    _pack_   =  1
    _fields_ =  [
                    ("_packet_len", c_uint16),
                    ("_control_ctr", c_uint16),
                ]

    def __init__(self, packet_len = 0x0000, control_ctr = 0x0000):
        self._packet_len  = packet_len
        selcf._control_ctr = control_ctr

    def update_control(self):
        """
        Increment control counter for flow control of Ethernet traffic.
        """
        self._control_ctr += 0x01

class EthernetTransport(TransportBase):
    """
    This class describes Ethernet transport layer used for XCP.
    XCP on Ethernet is adding an extra header to XCP frame.
    No tail is added.
    """
    def __init__(self):
        super(EthernetTransport, self).__init__()
        self._header = XcpEthernetHeader()

    def create_message(self, packet):
        """
        Creates a XCP Ethernet frame 

        :param      packet:  The packet to send.
        :type       packet:  XCPPacketBase
        
        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        self._header.packet_len = len(bytes(packet))
        
        frame_bytes = super(EthernetTransport, self).create_message(packet) 
        
        # Update control counter for next frame
        self._header.update_control()
        
        return bytes(frame_bytes)