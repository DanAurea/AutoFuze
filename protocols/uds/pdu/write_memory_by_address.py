import enum
import struct

from ctypes import c_uint8, c_uint16, c_uint32, c_uint64

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class WriteMemoryByAddress(ServiceBase):
    """
    Service allowing to write into memory.
    Usually used for clearing NVM or changing calibration values.
    """

    __slots__ = ('data', 'length_format', 'memory_address', 'memory_size',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.WRITE_MEMORY_BY_ADDRESS
    
    def __init__(self, data:bytes, parameters_length = 0x10, memory_address = 0x0000, memory_size = 0x0000):    
        self.length_memory_address = parameters_length & 0xF
        self.length_memory_size    = (parameters_length >> 4 ) & 0xF
        
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
        memory_address_format = 0 * c_uint8 # Optional by default
        
        if self.length_memory_address == 1:
            memory_address_format = c_uint8
        elif self.length_memory_address == 2:
            memory_address_format = c_uint16
        elif self.length_memory_address == 4:
            memory_address_format = c_uint32
        elif self.length_memory_address == 8:
            memory_address_format = c_uint64
        else:
            pass # TODO: Handle odd numbers and invalid values

        memory_size_format = 0 * c_uint8 # Optional by default

        if self.length_memory_size == 1:
            memory_size_format = c_uint8
        elif self.length_memory_size == 2:
            memory_size_format = c_uint16
        elif self.length_memory_size == 4:
            memory_size_format = c_uint32
        elif self.length_memory_size == 8:
            memory_size_format = c_uint64
        else:
            pass # TODO: Handle odd numbers and invalid values

        class Payload(ServiceBase):
            SERVICE_ID = WriteMemoryByAddress.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('length_format', c_uint8),
                            ('memory_address', memory_address_format),
                            ('memory_size', memory_size_format),
                            ('data', len(self.data) * c_uint8),
                        ]
        
        payload = Payload()
        payload.length_format = (self.length_memory_size << 4) | self.length_memory_address
        
        if sizeof(memory_address_format):
            payload.memory_address = self.memory_address

        if sizeof(memory_address_format):
            payload.memory_size = self.memory_size

        payload.data = (c_uint8 * len(self.data))(*self.data)

        return bytes(payload)