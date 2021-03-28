import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadMemoryByAddress(ServiceBase):
    """
    Service that read memory by specifying a memory address.
    """

    class SubFunction(enum.IntEnum):
        ENABLE = 0X01

    def __init__(self, sub_function = SubFunction.ENABLE): 
        self.service_id   = ServiceID.READ_MEMORY_BY_ADDRESS
        self.sub_function = sub_function

    def __bytes__(self):
        pass