import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class WriteDataByID(ServiceBase):
    """
    Write data on ECU by locating it with an ID.
    """

    __slots__ = ('did',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.WRITE_DATA_BY_IDENTIFIER
    
    def __init__(self, did = 0x0000):
        self.did = did

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2E)
        [1:3] : Data ID (DID)
        """

        b = bytearray()

        b.extend(super(WriteDataByID, self).__bytes__())
        b.extend(struct.pack("!H", self.did))

        return bytes(b)

    def __repr__(self):
        s = """{}
                DID: {}
            """.format  (
                            super(WriteDataByID, self).__repr__(),
                            self.did,
                        )

        return s