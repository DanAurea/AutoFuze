import enum
import struct

from ctypes import c_uint8, c_uint16

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class DynamicallyDefineDataID(ServiceBase):
    """
    Service allowing to subset several data identifier into one unique identifier.
    It's allow to read several data in a row when calling read data identifier service (0x22).
    """

    __slots__ = ('sub_function', 'defined_did', 'source_did' ,) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.DYNAMICALLY_DEFINE_DATA_IDENTIFIER
    
    class SubFunction(enum.IntEnum):
        DEFINE_BY_IDENTIFIER              = 0x01
        DEFINE_BY_MEMORY_ADDRESS_AND_SIZE = 0x02
        CLEAR_DEFINED_DID                 = 0x03

    def __init__(self, sub_function = SubFunction.DEFINE_BY_IDENTIFIER, defined_did = 0x0000, source_did = 0x0000, ): 
        self.sub_function = sub_function
        self.defined_did  = defined_did
        self.source_did   = source_did

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2C)
        [1:2] : Sub function
        [2:4] : Defined Data ID (DID)
        """
        class Payload(ServiceBase):
            SERVICE_ID = DynamicallyDefineDataID.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('defined_did', c_uint16)
                        ]

        payload = Payload()
        payload.defined_did = self.defined_did

        # TODO: Implement remaining logic.

        return bytes(payload)