from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class NegativeResponse(ServiceBase):

    def __init__(self):
        self.service_id = ServiceID.NEGATIVE_RESPONSE

    def __bytes__(self):
        pass