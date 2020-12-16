from xcp.client.base import ClientBase
from xcp.transport.ethernet import EthernetTransport

class EthernetClient(ClientBase):
    DEFAULT_XCP_PORT = 5555

    def __init__(self):
        super(EthernetClient, self).__init__()

        self._ecu_address     = "localhost"
        self._port            = self.DEFAULT_XCP_PORT
        
        self._transport_layer = EthernetTransport()
        self._slave_address   = (self._ecu_address, self._port)

    def send(self, packet):
        self._transport_layer.create_message(packet)

    def receive(self):
        pass