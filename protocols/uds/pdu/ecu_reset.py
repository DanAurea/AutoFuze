import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class EcuReset(ServiceBase):

    class SubFunction(enum.IntEnum):
        UNCONTROLLED = 0x01 # Hard reset
        CONTROLLED   = 0x02 # ON/OFF reset
        SOFT         = 0x03 # Soft reset

    def __init__(self, sub_function = self.SubFunction.CONTROLLED): 
        self.service_id   = ServiceID.ECU_RESET
        self.sub_function = sub_function

    def __bytes__(self):
        pass