import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class TesterPresent(ServiceBase):

    def __init__(self):
        self.service_id = ServiceID.TESTER_PRESENT
        
    def __bytes__(self):
        pass