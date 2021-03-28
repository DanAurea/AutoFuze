import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadScalingDataByID(ServiceBase):

    class SubFunction(enum.IntEnum):
        ENABLE = 0X01

    def __init__(self, sub_function = SubFunction.ENABLE): 
        self.service_id   = ServiceID.READ_SCALING_DATA_BY_IDENTIFIER
        self.sub_function = sub_function

    def __bytes__(self):
        pass