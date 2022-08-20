import enum
import struct

from ctypes import c_uint8, c_uint16

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

        # TODO: Update logic with length/format behaviour.
        class Payload(ServiceBase):
            SERVICE_ID = WriteMemoryByAddress.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('length_format', c_uint8),
                            ('memory_address', c_uint16),
                            ('memory_size', c_uint8),
                            ('data', len(self.data) * c_uint8),
                        ]

        payload = Payload()
        payload.length_format  = self.length_format
        payload.memory_address = self.memory_address
        payload.memory_size    = self.memory_size
        payload.data           = (c_uint8 * len(self.data))(*self.data)

        return bytes(payload)