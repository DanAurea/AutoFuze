from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.enum.nrc import NRC
from uds.pdu.base import ServiceBase

class NegativeResponse(ServiceBase):
    """
    Generic service that represents an error.
    Usually sent when something has gone wrong.
    """
    
    SERVICE_ID = ServiceID.NEGATIVE_RESPONSE

    _pack_   = 1
    _fields_ =  [
                    ('request_service_id', c_uint8),
                    ('nrc', c_uint8),
                ]

    def __init__(self, request_service_id, nrc):
        self.request_service_id = request_service_id
        self.nrc                = nrc

    def __repr__(self):
        s = """{}
                Requested service ID: {}
                NRC: {}
            """.format  (
                            super(NegativeResponse, self).__repr__(),
                            ServiceID(self.request_service_id).name,
                            NRC(self.nrc).name,
                        )

        return s