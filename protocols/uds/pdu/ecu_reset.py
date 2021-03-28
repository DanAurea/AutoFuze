import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class EcuReset(ServiceBase):
    """
    Service that reset ECU with different ways.
    """

    class SubFunction(enum.IntEnum):
        UNCONTROLLED = 0x01 # Hard reset
        CONTROLLED   = 0x02 # ON/OFF reset
        SOFT         = 0x03 # Soft reset

    def __init__(self, sub_function = SubFunction.CONTROLLED): 
        self.service_id   = ServiceID.ECU_RESET
        self.sub_function = sub_function

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x11)
        [1:2] : Sub function
        """

        b = bytearray()

        # Convert to big endian (network endianness)
        b.extend(super(EcuReset, self).__bytes__())
        b.extend(struct.pack('!B', self.sub_function))

        return bytes(b)

    def __repr__(self):
        s = """{}
                Sub function: {}
            """.format  (
                            super(EcuReset, self).__repr__(),
                            self.sub_function.name,
                        )

        return s