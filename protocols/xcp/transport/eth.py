class XcpEthHeader(object):
    """
    This class describes a XCP ethernet header.
    """

    def __init__(self, packet_len = 0x0000, control_ctr = 0x0000):
        self._packet_len  = packet_len
        self._control_ctr = control_ctr

    def __bytes__(self):
        pass

class EthTransport(TransportBase):

    def __init__(self):
        super(TransportBase, self).__init__()
        self._header = XcpEthHeader()

    def create_message(self, packet):
        super(TransportBase, self.create_message(packet))