import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadMemoryByAddress(ServiceBase):

    class SubFunction(enum.IntEnum):
        ENABLE = 0X01

    def __init__(self, sub_function = self.SubFunction.ENABLE): 
        self.service_id   = ServiceID.READ_MEMORY_BY_ADDRESS
        self.sub_function = sub_function

    def __bytes__(self):
        pass