from network.ethernet import Ethernet
from xcp.client.base import ClientBase
from xcp.transport.ethernet import EthernetTransport

class EthernetClient(ClientBase):
    DEFAULT_XCP_PORT = 5555

    def __init__(self):
        super(EthernetClient, self).__init__()

        self._ecu_address     = "localhost"
        self._port            = self.DEFAULT_XCP_PORT
        
        self._transport_layer = EthernetTransport()
        
        self._physical_layer  = Ethernet()
        self._slave_address   = (self._ecu_address, self._port)

    def send(self, packet):
        """
        Send frame over Ethernet layer.
        
        :param      packet:  The packet
        :type       packet:  { type_description }
        """
        frame = super(EthernetClient, self).get_frame(packet)

    def receive(self):
        pass