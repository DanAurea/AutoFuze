import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class SecuredDataTransmission(ServiceBase):

    SERVICE_ID = ServiceID.SECURED_DATA_TRANSMISSION
            
    def __bytes__(self):
        pass