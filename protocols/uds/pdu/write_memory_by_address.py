import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class WriteMemoryByAddress(ServiceBase):
    """
    This class describes a write memory by address.
    """

    def __init__(self, address = 0x0000):
        self.service_id = ServiceID.WRITE_DATA_BY_IDENTIFIER
        self.address    = address
                
    def __bytes__(self):
        pass