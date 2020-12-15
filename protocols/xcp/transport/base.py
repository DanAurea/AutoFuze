class TransportBase(object):
    """
    This class describes the transport layer basis.
    
    In XCP header and tail are dependent of transport layer so this
    is providing a way to redefine behavior depending on which transport
    layer is used.
    """

    def __init__(self):
        self._header = None
        self._tail   = None

    def create_message(self, packet):
        """
        Creates a message independtly of its transport layer.
        Sub classes should overload this method if they want to
        add transport dependent behavior.

        :param      packet:  The packet to send.
        :type       packet:  PacketBase
        
        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        message_bytes = bytearray()

        if self._header:
            message_bytes.extend(bytes(self._header))

        message_bytes.extend(bytes(packet))

        if self._tail:
            message_bytes.extend(bytes(self._tail))

        return bytes(message_bytes)