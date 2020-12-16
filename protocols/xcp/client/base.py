class ClientBase(object):
    
    def __init__(self):
        self._transport_layer = None

    def send(self, packet):
        pass

    def receive(self):
        pass