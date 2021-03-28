import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class CommunicationControl(ServiceBase):

    class SubFunction(enum.IntEnum):
        ENABLE = 0x01

    class Communication(enum.IntEnum):
        ENABLE_RX  = ENABLE_TX = 0x00
        DISABLE_TX = 0x01
        DISABLE_RX = 0x02

    def __init__(self, sub_function = self.SubFunction.ENABLE, communication = self.Communication.ENABLE_TX): 
        self.service_id   = ServiceID.COMMUNICATION_CONTROL
        self.sub_function = sub_function

    def __bytes__(self):
        pass