from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class NegativeResponse(ServiceBase):
    """
    Generic service that represents an error.
    Usually sent when something has gone wrong.
    """
    
    SERVICE_ID = ServiceID.NEGATIVE_RESPONSE

    def __bytes__(self):
        pass