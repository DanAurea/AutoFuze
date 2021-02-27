from xcp.transport.base import TransportBase
from struct import pack

class UsbHeader(object):
    """
    This class describes a USB header.
    USB composition vary regarding XCP packet
    
    """
    def __init__(self):
        self._packet_len  = 0x00
        self._control_ctr = 0x00

    def update_control(self):
        """
        Increment control counter for flow control of Ethernet traffic.
        """
        self._control_ctr += 0x01

    def __bytes__(self):
        """
        Return bytes representation of USB header.
        """
        header_bytes = bytearray()

        header_bytes.extend(pack("<B", self._packet_len))
        header_bytes.extend(pack("<B", self._control_ctr))

        return b''

class UsbTail(object):

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
        :type       packet:  PacketBase
        
        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        
        frame_bytes = super(UsbTransport, self).create_message(packet)
        self._header.update_control()

        return bytes(frame_bytes)