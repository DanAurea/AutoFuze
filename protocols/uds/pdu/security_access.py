import enum
import struct

from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class SecurityAccess(ServiceBase):
    """
    Service allowing to unlock secured services.

    Unlock process follows this sequence flow:
    
    Tester: Request seed
    ECU: Provide a seed
    Tester: Compute key from seed with a determined cipher (OEM dependent).
    Tester: Send back the key
    ECU: Answer with ACK/NACK
    """

    __slots__ = ('key', 'sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.SECURITY_ACCESS
    
    class SubFunction(enum.IntEnum):
        REQUEST_SEED = 0x01 # Odd numbers
        SEND_KEY     = 0x02 # Even numbers

    def __init__(self, sub_function = SubFunction.REQUEST_SEED, level = 0, key = b''):
        self.sub_function = sub_function # TODO: Define sub_function calculation based on level (@property ?)
        self.key          = key
    
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x27)
        [1:2] : Sub function
        [2:N] : Key (Optional)
        """
        if (self.sub_function % self.SubFunction.SEND_KEY) == 0:
            class Payload(ServiceBase):
                SERVICE_ID = SecurityAccess.SERVICE_ID
                _pack_   = 1
                _fields_ =  [
                                ('sub_function', c_uint8),
                                ('key', len(self.key) * c_uint8),
                            ]

            payload = Payload()
            payload.sub_function = self.sub_function
            payload.key = (len(self.key) * c_uint8)(*self.key)
        else:
            class Payload(ServiceBase):
                SERVICE_ID = SecurityAccess.SERVICE_ID
                _pack_   = 1
                _fields_ =  [
                                ('sub_function', c_uint8),
                            ]

            payload = Payload()
            payload.sub_function = self.sub_function

        return bytes(payload)

    def __repr__(self):
        s = """{}
                Sub function: {}
            """.format  (
                            super(SecurityAccess, self).__repr__(),
                            self.sub_function.name,
                        )

        if self.sub_function == self.SubFunction.SEND_KEY:
            s += str(self.key)

        return s        