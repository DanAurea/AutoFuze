from ctypes import LittleEndianStructure

class XCPTransportBase(LittleEndianStructure):
    """
    This class describes the transport layer basis.
    
    In XCP header and tail are dependent of transport layer so this
    is providing a way to redefine behavior depending on which transport
    layer is used.
    """

    def __new__(cls, *args, **kwargs):
        instance         = super(XCPTransportBase, cls).__new__(cls, *args, **kwargs)
        instance._header = b'' # Identification is empty by default
        instance._pdu    = b'' # PDU is empty by default
        instance._tail   = b'' # Timestamp is empty by default

        return instance

    def __truediv__(self, pdu):
        """
        Override true division operator so packet crafting will be prettier.
        
        :param      payload:  The payload
        :type       payload:  PayloadType
        
        :returns:   The final DoIP message
        :rtype:     bytes
        """
        if pdu:
            self._pdu = pdu
        else:
            # TODO: Log warning diagnostic PDU can't be empty ?
            pass

        return self

    def __bytes__(self):
        """
        Creates a message independtly of its transport layer.
        Sub classes should overload this method if they want to
        add transport dependent behavior.
        
        :returns:   Bytes of the message related to its transport layer.
        :rtype:     bytes
        """
        return bytes(self._header) + bytes(self._pdu) + bytes(self._tail)