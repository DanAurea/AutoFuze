from xcp.transport.base import TransportBase
from struct import pack

class XcpEthernetHeader(object):
    """
    This class describes a XCP ethernet header.*
    XCP Ethernet header is composed as:
        - 2 bytes describing XCP Packet Length
        - 2 bytes describing a control ctr (used to detect missing packets in flow control)
    """

    def __init__(self, packet_len = 0x0000, control_ctr = 0x0000):
        self._packet_len  = packet_len
        self._control_ctr = control_ctr

    def _set_packet_len(self, packet_len):
        """
        Set the packet length.
        
        :param      packet_len:  The packet length
        :type       packet_len:  unsigned int
        """
        self._packet_len = packet_len

    def update_control(self):
        """
        Increment control counter for flow control of Ethernet traffic.
        """
        self._control_ctr += 0x01

    def __bytes__(self):
        """
        Return bytes representation of Ethernet header.
        """
        return pack("<HH", self._packet_len, self._control_ctr)

    packet_len = property(fset = _set_packet_len)
    del _set_packet_len

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
        :type       packet:  PacketBase
        
        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        self._header.packet_len = len(bytes(packet))
        
        frame_bytes = super(EthernetTransport, self).create_message(packet) 
        
        # Update control counter for next frame
        self._header.update_control()
        
        return bytes(frame_bytes)