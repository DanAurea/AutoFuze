import enum
import struct

from ctypes import c_uint8

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
        STORE_EVENT                  = 0X40

    _pack_   = 1
    _fields_ =  [
                    ('sub_function', c_uint8),
                ]

    def __init__(self, sub_function = SubFunction.ON_DTC_STATUS_CHANGE):
        self.sub_function = sub_function

    def __repr__(self):
        s = """{}
                Sub function: {}
            """.format  (
                            super(ResponseOnEvent, self).__repr__(),
                            self.SubFunction(self.sub_function).name,
                        )

        return s