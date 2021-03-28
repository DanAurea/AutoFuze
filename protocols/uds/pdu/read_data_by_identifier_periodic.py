import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadDataByIDPeriodic(ServiceBase):

    def __init__(self, did = 0x0000): 
        self.service_id = ServiceID.READ_DATA_BY_IDENTIFIER_PERIODIC
        self.did        = did

    def __bytes__(self):
        pass