import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class WriteMemoryByAddress(ServiceBase):
    """
    Service allowing to write into memory.
    Usually used for clearing NVM or changing calibration values.
    """

    __slots__ = ('data', 'length_format', 'memory_address', 'memory_size',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.WRITE_DATA_BY_IDENTIFIER
    
    def __init__(self, data:bytes, length_format = 0x10, memory_address = 0x0000):    
        self.length_format  = length_format
        self.memory_address = memory_address
        self.memory_size    = memory_size
        self.data           = data
                
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x3D)
        [1:2] : Length format
        [2:4] : Memory address
        [4:5] : Memory size
        [5:N] : Data
        """

        b = bytearray()

        b.extend(super(WriteMemoryByAddress, self).__bytes__())
        b.extend(struct.pack("!B", self.length_format))

        # TODO: Implement write by memory logic

        return bytes(b)