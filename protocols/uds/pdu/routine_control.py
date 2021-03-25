import enum
import sys
import struct

sys.path.append("../../")
from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RoutineControl(ServiceBase):
    """
    This class describes a routine control service.
    Routine control allows to run some routines on ECU based on an ID.
    """

    class SubFunction(enum.IntEnum):
        START           = 0x01
        STOP            = 0x02
        REQUEST_RESULTS = 0x03

    def __init__(self, sub_function = SubFunction.START, routine_id = 0x0000):
        self.service_id   = ServiceID.ROUTINE_CONTROL
        self.sub_function = self.SubFunction.START
        self.routine_id   = routine_id

    def __bytes__(self):
        """
        Interpret the object as a sequence of bytes that will be used for
        request delivery.
        """
        b = bytearray()

        # Convert to big endian (network endianness)
        b.extend(super(RoutineControl, self).__bytes__())
        b.extend(struct.pack('!B', self.sub_function))
        b.extend(struct.pack('!H', self.routine_id))

        return b

    def __repr__(self):
        s = '''{}
                Sub function: {}
                Routine ID: {}
            '''.format  (
                            super(RoutineControl, self).__repr__(),
                            self.SubFunction(self.sub_function).name,
                            self.routine_id
                        )

        return s