import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class AccessTimingParameters(ServiceBase):
    """
    Access timing parameters in which each request/response should
    be send before timer expires.

    Tester can change timing parameters to given values.
    """

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.ACCESS_TIMING_PARAMETERS

    class SubFunction(enum.IntEnum):
        READ_EXTENDED_TIMING_PARAMETER_SET      = 0x01
        SET_TIMING_PARAMETERS_TO_DEFAULT_VALUES = 0x02
        READ_CURRENTLY_ACTIVE_TIMING_PARAMETERS = 0x03
        SET_TIMING_PARAMETERS_TO_GIVEN_VALUES   = 0x04

    def __init__(self, sub_function = 0x0, timing_param_record = ): 
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

        # Set ECU timeouts to user desired values, this will impact sequence flow of
        # subsequent requests and timing to meet.
        if self.sub_function == self.SubFunction.SET_TIMING_PARAMETERS_TO_GIVEN_VALUES:
            pass

        return bytes(b)

    def __repr__(self):
        s = """{}
                Sub function: {}
            """.format  (
                            super(AccessTimingParameters, self).__repr__(),
                            self.sub_function.name,
                        )

        return s