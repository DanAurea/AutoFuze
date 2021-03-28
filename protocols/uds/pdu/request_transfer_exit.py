import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestTransferExit(ServiceBase):

    def __init__(self): 
        self.service_id = ServiceID.REQUEST_TRANSFER_EXIT
        
    def __bytes__(self):
        pass