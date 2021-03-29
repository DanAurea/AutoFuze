import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadDataByID(ServiceBase):
    """
    Service that read a data into ECU's memory by referring to a Data ID (DID).
    """

    def __init__(self, did = 0x0000): 
        self.service_id = ServiceID.READ_DATA_BY_IDENTIFIER
        self.did        = did

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x22)
        [1:3] : Data ID (DID)
        """

        b = bytearray()

        b.extend(super(ReadDataByID, self).__bytes__())
        b.extend(struct.pack("!H", self.did))

        return bytes(b)

    def __repr__(self):
        s = """{}
                DID: {}
            """.format  (
                            super(ReadDataByID, self).__repr__(),
                            self.did,
                        )

        return s