import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadMemoryByAddress(ServiceBase):
    """
    Service that read memory by specifying a memory address.
    """
    
    __slots__ = ('length_format', 'memory_address',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.READ_MEMORY_BY_ADDRESS

    def __init__(self, length_format = 0x11, memory_address = 0x0000): 

        self.length_format  = length_format
        self.memory_address = memory_address

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x23)
        [1:2] : Length format
        [2:N] : Memory address
        """

        b = bytearray()

        b.extend(super(ReadMemoryByAddress, self).__bytes__())
        #TODO: Implement read data by memory logic
        
        return bytes(b)