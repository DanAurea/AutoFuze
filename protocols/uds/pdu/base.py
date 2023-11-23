import struct

from ctypes import LittleEndianStructure, c_uint8

from uds.enum.service_id import ServiceID

class ServiceBase(LittleEndianStructure):
    """
    This class describes a unified diagnostic service (UDS) base.
    """
    SERVICE_ID = ServiceID.NEGATIVE_RESPONSE

    _pack_   = 1
    _fields_ =  [
                    ('service_id', c_uint8),
                ]

    def __new__(cls, *args, **kwargs):
        instance             = super(ServiceBase, cls).__new__(cls, *args, **kwargs)
        instance.service_id = cls.SERVICE_ID
        return instance

    def __repr__(self):
        """
        Describe an object representation of Service that will helps for debugging purpose.
        PDU is the full list of bytes formed from user request. 
        """

        s = """PDU: {}
                Service ID: {}""".format(
                                            [hex(b) for b in bytes(self)],
                                            self.SERVICE_ID.name
                                        )

        return s