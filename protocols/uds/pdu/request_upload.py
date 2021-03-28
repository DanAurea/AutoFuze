import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestUpload(ServiceBase):

    def __init__(self): 
        self.service_id = ServiceID.REQUEST_UPLOAD
        
    def __bytes__(self):
        pass