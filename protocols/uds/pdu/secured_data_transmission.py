import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class SecuredDataTransmission(ServiceBase):

    def __init__(self):
        self.service_id = ServiceID.SECURED_DATA_TRANSMISSION
        
    def __bytes__(self):
        pass