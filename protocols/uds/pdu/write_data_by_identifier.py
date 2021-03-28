import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class WriteDataByID(ServiceBase):
    """
    This class describes a write data by id.
    """

    def __init__(self, did = 0x0000):
        self.service_id = ServiceID.WRITE_DATA_BY_IDENTIFIER
        self.did        = did

    def __bytes__(self):
        pass