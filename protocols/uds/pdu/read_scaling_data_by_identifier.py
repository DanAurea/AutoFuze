import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadScalingDataByID(ServiceBase):

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID   = ServiceID.READ_SCALING_DATA_BY_IDENTIFIER
    
    class SubFunction(enum.IntEnum):
        ENABLE = 0X01

    def __init__(self, sub_function = SubFunction.ENABLE): 
        self.sub_function = sub_function

    def __bytes__(self):
        pass