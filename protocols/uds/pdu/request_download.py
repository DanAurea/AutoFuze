import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestDownload(ServiceBase):
    """
    Service allowing to start a download between tester and ECU.
    Commonly used for flash updates.
    
    Any other values than 0x00 for encryption/compression is OEM specific.
    No encryption  = 0x00
    No compression = 0x00
    """
    
    __slots__ = ('data_format', 'memory_address', 'memory_size', 'length_memory_address', 'length_memory_size',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.REQUEST_DOWNLOAD

    def __init__(self, data_format = 0x00, parameters_length = 0x44, memory_address = 0x00, memory_size = 0x00):
        self.data_format           = data_format # [0:4] Encyrption method; [4:8] Compression method
        
        self.length_memory_address = parameters_length & 0xFF
        self.length_memory_size    = (parameters_length >> 4 ) & 0xFF
        
        self.memory_address        = memory_address
        self.memory_size           = memory_size

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X34)
        [1:2]: Data format (Encyrption method / Compression method)
        [2:3]: Length of memory address | Length memory size
        [3:N]: Memory address
        [N:M]: Memory size
        """

        b = bytearray()

        b.extend(super(RequestDownload, self).__bytes__())
        b.extend(data_format)
        b.extend(struct.pack("!B", self.length_memory_address | self.length_memory_size << 4))

        memory_address_encoding = "B"

        if length_memory_address == 2:
            memory_address_encoding = "H"
        elif length_memory_address == 4:
            memory_address_encoding = "I"
        elif length_memory_address == 8:
            memory_address_encoding = "Q"

        if memory_address_encoding == "B": # Encode byte by byte in case user would like to fuzz with odd number of bytes.
            b.extend(struct.pack("!" + self.length_memory_address * "B", self.memory_address))
        else:
            b.extend(struct.pack("!" + memory_address_encoding, self.memory_address))

        memory_size_encoding = "B"

        if length_memory_size == 2:
            memory_size_encoding = "H"
        elif length_memory_size == 4:
            memory_size_encoding = "I"
        elif length_memory_size == 8:
            memory_size_encoding = "Q"

        if memory_size_encoding == "B":
            b.extend(struct.pack("!" + self.length_memory_size * "B", self.memory_size))
        else:
            b.extend(struct.pack("!" + memory_size_encoding, self.memory_size))

        return bytes(b)

        def __repr__(self):
            s = """{}
                Data format: {}
                Length memory address: {}
                Length memory size: {}
                Memory address: {}
                Memory size: {}
                """.format  (
                            super(RequestDownload, self).__repr__(),
                            self.data_format,
                        )

        return s