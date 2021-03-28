import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class IOControlByID(ServiceBase):

    class SubFunction(enum.IntEnum):
        ENABLE = 0x01

    def __init__(self, sub_function = self.SubFunction.ENABLE): 
        self.service_id   = ServiceID.INPUT_OUTPUT_CONTROL_BY_IDENTIFIER
        self.sub_function = sub_function

    def __bytes__(self):
        pass