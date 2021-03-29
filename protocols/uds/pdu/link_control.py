import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class LinkControl(ServiceBase):
    """
    Service that control link status.
    """

    class SubFunction(enum.IntEnum):
        VERIFY_BAUDRATE_TRANSITION_WITH_FIXED_BAUDRATE    = 0x01
        VERIFY_BAUDRATE_TRANSITION_WITH_SPECIFIC_BAUDRATE = 0x02
        TRANSITION_BAUDRATE                               = 0x03

    def __init__(self, sub_function = SubFunction.VERIFY_BAUDRATE_TRANSITION_WITH_FIXED_BAUDRATE): 
        self.service_id   = ServiceID.LINK_CONTROL
        self.sub_function = sub_function

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x87)
        [1:2] : Sub function
        """

        b = bytearray()

        b.extend(super(LinkControl, self).__bytes__())
        b.extend(struct.pack("!B", self.sub_function))

        return bytes(b)