import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class DynamicallyDefineDataID(ServiceBase):
    """
    Service allowing to subset several data identifier into one unique identifier.
    It's allow to read several data in a row when calling read data identifier service (0x22).
    """

    __slots__ = ('did', 'sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.DYNAMICALLY_DEFINE_DATA_IDENTIFIER
    
    class SubFunction(enum.IntEnum):
        DEFINE_BY_IDENTIFIER              = 0x01
        DEFINE_BY_MEMORY_ADDRESS_AND_SIZE = 0x02
        DEFINE_BY_IDENTIFIER_AND_MEMORY   = 0x03

    def __init__(self, sub_function = SubFunction.DEFINE_BY_IDENTIFIER, did = 0x0000): 
        self.sub_function = sub_function
        self.did          = did

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2C)
        [1:2] : Sub function
        [2:4] : Data ID (DID)
        """

        b = bytearray()

        b.extend(super(DynamicallyDefineDataID, self).__bytes__())
        b.extend(struct.pack("!B", self.sub_function))

        # TODO: Implement logic related to sub function
        if self.sub_function == self.SubFunction.DEFINE_BY_IDENTIFIER:
            b.extend(struct.pack("!H", self.did))

        return bytes(b)