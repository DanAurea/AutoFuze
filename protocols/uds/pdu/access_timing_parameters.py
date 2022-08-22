import enum
import struct

from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class AccessTimingParameters(ServiceBase):
    """
    Access timing parameters in which each request/response should
    be send before timer expires.

    Tester can change timing parameters to given values.
    """

    __slots__ = ('sub_function', 'timing_param_record') # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.ACCESS_TIMING_PARAMETERS

    class SubFunction(enum.IntEnum):
        READ_EXTENDED_TIMING_PARAMETER_SET      = 0x01
        SET_TIMING_PARAMETERS_TO_DEFAULT_VALUES = 0x02
        READ_CURRENTLY_ACTIVE_TIMING_PARAMETERS = 0x03
        SET_TIMING_PARAMETERS_TO_GIVEN_VALUES   = 0x04

    def __init__(self, sub_function = SubFunction.READ_CURRENTLY_ACTIVE_TIMING_PARAMETERS, timing_param_record:bytes = b''): 
        self.sub_function        = sub_function
        self.timing_param_record = timing_param_record

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x83)
        [1:2] : Sub function
        """
        timing_param_record_format = 0 * c_uint8
        
        if self.sub_function == self.SubFunction.SET_TIMING_PARAMETERS_TO_GIVEN_VALUES:
            timing_param_record_format = len(self.timing_param_record) * c_uint8

        class Payload(ServiceBase):
            SERVICE_ID = AccessTimingParameters.SERVICE_ID
            _pack_ = 1
            _fields_ = [
                            ('sub_function', c_uint8),
                            ('timing_param_record', timing_param_record_format),
                        ]

        payload = Payload()
        payload.sub_function = self.sub_function

        # Set ECU timeouts to user desired values, this will impact sequence flow of
        # subsequent requests and timing to meet.
        if self.sub_function == self.SubFunction.SET_TIMING_PARAMETERS_TO_GIVEN_VALUES:
            payload.timing_param_record = (len(self.timing_param_record) * c_uint8)(*self.timing_param_record)

        return bytes(payload)

    def __repr__(self):
        s = """{}
                Sub function: {}
                Timing parameter record: {}
            """.format  (
                            super(AccessTimingParameters, self).__repr__(),
                            self.SubFunction(self.sub_function).name,
                            self.timing_param_record,
                        )

        return s