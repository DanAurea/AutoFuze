class ClientBase(object):
    """
    This class describes a client base and is used to serve as 
    a messaging system between Master and Slave.
    Master class could be defined by user reusing this class with
    composition.

    Some master implementation has been done to provide a quick
    access to XCP for anyone wanting to use the protocol without
    requirement to have flexibility over communication sequence etc... 
    """

    def __init__(self):
        self._transport_layer = None
        self._physical_layer  = None

    def get_frame(self, packet):
        """
        Gets the XCP frame formed with current transport
        layer set in client.
        
        :param      packet:  The packet
        :type       packet:  PacketBase
        
        :returns:   The XCP frame.
        :rtype:     TransportBase
        """

        if not self._transport_layer:
            # TODO: Log into debug level
            return

        # Create a XCP frame related to current transport
        return self._transport_layer.create_message(packet)

    def send(self, packet):
        pass

    def receive(self):
        pass