import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class LinkControl(ServiceBase):
    """
    Service that control link status.
    """

    class SubFunction(enum.IntEnum):
        ENABLE = 0x01

    def __init__(self, sub_function = SubFunction.ENABLE): 
        self.service_id   = ServiceID.LINK_CONTROL
        self.sub_function = sub_function

    def __bytes__(self):
        pass