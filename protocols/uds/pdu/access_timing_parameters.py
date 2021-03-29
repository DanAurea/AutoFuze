import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class AccessTimingParameters(ServiceBase):

    class SubFunction(enum.IntEnum):
        READ_EXTENDED_TIMING_PARAMETER_SET      = 0x01
        SET_TIMING_PARAMETERS_TO_DEFAULT_VALUES = 0x02
        READ_CURRENTLY_ACTIVE_TIMING_PARAMETERS = 0x03
        SET_TIMING_PARAMETERS_TO_GIVEN_VALUES   = 0x04

    def __init__(self, sub_function = 0x0): 
        self.service_id   = ServiceID.ACCESS_TIMING_PARAMETERS
        self.sub_function = sub_function

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x83)
        [1:2] : Sub function
        """

        b = bytearray()

        b.extend(super(AccsTimingParameters, self).__bytes__())
        b.extend(struct.pack("!B", self.sub_function))

        # TODO: Implement set values mechanism (ECU timeouts)

        return bytes(b)

    def __repr__(self):
        s = """{}
                Sub function: {}
            """.format  (
                            super(AccessTimingParameters, self).__repr__(),
                            self.sub_function.name,
                        )

        return s