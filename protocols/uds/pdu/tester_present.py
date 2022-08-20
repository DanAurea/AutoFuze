import enum

from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class TesterPresent(ServiceBase):
    """
    Service that allows to keep session alive on ECU. 
    Some timeouts can be included on ECU's session that will kick-off user 
    from current session. Sending tester present regularly avoid being kicked.
    """

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.TESTER_PRESENT
    
    class SubFunction(enum.IntEnum):
        NONE          = 0x00
        SUPRESS_REPLY = 0x80

    _pack_   = 1
    _fields_ =  [
                    ('_sub_function', c_uint8)
                ]

    def __init__(self, sub_function = SubFunction.SUPRESS_REPLY):
        self.sub_function = self._sub_function = sub_function

    def __repr__(self):
        s = """{}
                Sub function: {}
            """.format  (
                            super(TesterPresent, self).__repr__(),
                            self.sub_function.name,
                        )

        return s