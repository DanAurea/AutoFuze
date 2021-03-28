import struct

from uds.enum.service_id import ServiceID

class ServiceBase(object):
    """
    This class describes a unified diagnostic service (UDS) base.
    """

    def __new__(cls, *args, **kwargs):
        instance            = super(ServiceBase, cls).__new__(cls, *args, **kwargs)
        instance.service_id = ServiceID.NEGATIVE_RESPONSE 
        return instance

    def __init__(self):
        pass

    def __bytes__(self):
        """
        Return service id as a byte (common for all services)
        
        :returns:   service_id
        :rtype:     byte
        """
        return struct.pack("!B", self.service_id)

    def __repr__(self):
        """
        Describe an object representation of Service that will helps for debugging purpose.
        PDU is the full list of bytes formed from user request. 
        """

        s = """PDU: {}
                Service ID: {}""".format(
                                            [hex(b) for b in self.__bytes__()],
                                            ServiceID(self.service_id).name
                                        )

        return s