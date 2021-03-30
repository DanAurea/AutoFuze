import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ResponseOnEvent(ServiceBase):
    """
    Service allowing to control flow of response from ECU.
    Based on some events ECU can start/stop to transmit response.
    """

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.RESPONSE_ON_EVENT
    
    class SubFunction(enum.IntEnum):
        STOP_RESPONSE_ON_EVENT       = 0X00
        ON_DTC_STATUS_CHANGE         = 0X01
        ON_TIMER_INTERRUPT           = 0X02
        ON_CHANGE_OF_DATA_IDENTIFIER = 0X03
        REPORT_ACTIVATED_EVENTS      = 0X04
        START_RESPONSE_EVENTS        = 0X05
        CLEAR_RESPONSE_EVENTS        = 0X06
        ON_COMPARISON_OF_VALUES      = 0X07

    def __init__(self, sub_function = SubFunction.ON_DTC_STATUS_CHANGE):
        self.sub_function = sub_function
        
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X86)
        [1:2]: Sub function
        """

        b = bytearray()

        b.extend(super(ResponseOnEvent, self).__bytes__())
        b.extend(struct.pack("!B", self.sub_function))

        # TODO: Check whether logic is fully implemented or not.

        return bytes(b)