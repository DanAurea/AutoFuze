import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ControlDTCSettings(ServiceBase):

    class SubFunction(enum.IntEnum):
        ENABLE = 0x01

    def __init__(self, sub_function = self.SubFunction.ENABLE, settings = []): 
        self.service_id   = ServiceID.CONTROL_DTC_SETTINGS
        self.sub_function = sub_function
        self.settings     = settings

    def __bytes__(self):
        pass