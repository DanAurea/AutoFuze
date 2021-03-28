import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class CommunicationControl(ServiceBase):
    """
    Service that set communication state, ECU reception/transmission of
    requests can be controlled with this one.
    Can be used to disable transmission of some answer during critical
    process (flash etc...)
    """

    class SubFunction(enum.IntEnum):
        ENABLE = 0x01

    class Communication(enum.IntEnum):
        ENABLE_RX  = ENABLE_TX = 0x00
        DISABLE_TX = 0x01
        DISABLE_RX = 0x02

    def __init__(self, sub_function = SubFunction.ENABLE, communication = Communication.ENABLE_TX): 
        self.service_id   = ServiceID.COMMUNICATION_CONTROL
        self.sub_function = sub_function

    def __bytes__(self):
        pass