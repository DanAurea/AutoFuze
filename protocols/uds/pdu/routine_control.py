import enum
import struct

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

    def __init__(self, sub_function = SubFunction.START, routine_id = 0x0000):
        self.sub_function = self.SubFunction.START
        self.routine_id   = routine_id

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : Service ID (0x31)
        [1:2] : Sub function
        [2:4] : Routine ID
        """
        b = bytearray()

        # Convert to big endian (network endianness)
        b.extend(super(RoutineControl, self).__bytes__())
        b.extend(struct.pack('!B', self.sub_function))
        b.extend(struct.pack('!H', self.routine_id))

        return bytes(b)

    def __repr__(self):
        s = """{}
                Sub function: {}
                Routine ID: {}
            """.format  (
                            super(RoutineControl, self).__repr__(),
                            self.SubFunction(self.sub_function).name,
                            self.routine_id
                        )

        return s