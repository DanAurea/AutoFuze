import enum
import struct

from ctypes import c_uint8, c_uint16

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class WriteDataByID(ServiceBase):
    """
    Write data on ECU by locating it with an ID.
    """

    __slots__ = ('did', 'data',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.WRITE_DATA_BY_IDENTIFIER
    
    def __init__(self, did = 0x0000, data:bytes = b''):
        self.did  = did
        self.data = data

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2E)
        [1:3] : Data ID (DID)
        [3:N] : Data
        """
        class Payload(ServiceBase):
            SERVICE_ID = WriteDataByID.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('did', c_uint16),
                            ('data', len(self.data) * c_uint8),
                        ]

        payload = Payload()
        payload.did = self.did
        payload.data = (c_uint8 * len(self.data))(*self.data)

        return bytes(payload)

    def __repr__(self):
        s = """{}
                DID: 0x{:04X}
                Data: {}
            """.format  (
                            super(WriteDataByID, self).__repr__(),
                            self.did,
                            [hex(b) for b in self.data]
                        )

        return s