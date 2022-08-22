import enum

from ctypes import c_uint8, c_uint16, c_uint32, c_uint64, sizeof

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestUpload(ServiceBase):
    """
    Service allowing to read the downloaded firmware from ECU.
    """

    __slots__ = ('data_format', 'memory_address', 'memory_size', 'length_memory_address', 'length_memory_size',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID     = ServiceID.REQUEST_UPLOAD
    
    def __init__(self, data_format = 0x00, parameters_length = 0x44, memory_address = 0x0000, memory_size = 0x0000):    
        self.data_format           = data_format # [0:4] Encyrption method; [4:8] Compression method

        self.length_memory_address = parameters_length & 0xF
        self.length_memory_size    = (parameters_length >> 4 ) & 0xF

        self.memory_address        = memory_address # Mandatory field
        self.memory_size           = memory_size # Mandatory field
        
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X35)
        [1:N]: Memory address
        [N:M]: Memory size
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
            SERVICE_ID = RequestUpload.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('data_format', c_uint8),
                            ('length_format', c_uint8),
                            ('memory_address', memory_address_format),
                            ('memory_size', memory_size_format),
                        ]
        
        payload = Payload()
        payload.data_format   = self.data_format
        payload.length_format = (self.length_memory_size << 4) | self.length_memory_address
        
        if sizeof(memory_address_format):
            payload.memory_address = self.memory_address

        if sizeof(memory_address_format):
            payload.memory_size = self.memory_size

        return bytes(payload)

    def __repr__(self):
        s = """{}
            Data format: 0x{:04X}
            Length memory address: {}
            Length memory size: {}
            Memory address: 0x{:04X}
            Memory size: 0x{:04X}
            """.format  (
                        super(RequestUpload, self).__repr__(),
                        self.data_format,
                        self.length_memory_address,
                        self.length_memory_size,
                        self.memory_address,
                        self.memory_size,
                    )

        return s