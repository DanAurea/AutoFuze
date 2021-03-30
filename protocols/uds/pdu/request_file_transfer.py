import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestFileTransfer(ServiceBase):
    
    SERVICE_ID = ServiceID.REQUEST_FILE_TRANSFER
        
    def __bytes__(self):
        pass