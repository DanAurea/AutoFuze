import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ControlDTCSettings(ServiceBase):
    """
    Control DTC policy.
    """

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.CONTROL_DTC_SETTINGS
    
    class SubFunction(enum.IntEnum):
        ON  = 0x01
        OFF = 0x02

    def __init__(self, sub_function = SubFunction.ON, settings = []): 
        self.sub_function = sub_function

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x85)
        [1:2] : Sub function
        """

        b = bytearray()

        b.extend(super(ControlDTCSettings, self).__bytes__())
        b.extend(struct.pack("!B", self.sub_function))

        return bytes(b)

    def __repr__(self):
        s = """{}
                Sub function: {}
            """.format  (
                            super(ControlDTCSettings, self).__repr__(),
                            self.sub_function.name,
                        )

        return s