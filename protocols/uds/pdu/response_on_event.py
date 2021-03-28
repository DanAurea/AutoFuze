import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ResponseOnEvent(ServiceBase):

    def __init__(self):
        self.service_id = ServiceID.RESPONSE_ON_EVENT
        
    def __bytes__(self):
        pass