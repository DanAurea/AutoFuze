import enum
import struct

from ctypes import c_uint8, c_uint16

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RoutineControl(ServiceBase):
    """
    Routine control allows to run some routines on ECU based on an ID.
    """

    __slots__ = ('sub_function', 'routine_id',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID   = ServiceID.ROUTINE_CONTROL
    
    class SubFunction(enum.IntEnum):
        START           = 0x01
        STOP            = 0x02
        REQUEST_RESULTS = 0x03

    _pack_   = 1
    _fields_ =  [
                    ('sub_function', c_uint8),
                    ('routine_id', c_uint16),
                ]

    def __init__(self, sub_function = SubFunction.START, routine_id = 0x0000):
        self.sub_function = self.SubFunction.START
        self.routine_id   = routine_id

    def __repr__(self):
        s = """{}
                Sub function: {}
                Routine ID: 0x{:04X}
            """.format  (
                            super(RoutineControl, self).__repr__(),
                            self.SubFunction(self.sub_function).name,
                            self.routine_id
                        )

        return s