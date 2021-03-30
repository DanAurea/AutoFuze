import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class TransferData(ServiceBase):
    """
    Service that transfer data over a stream of block sequenced
    by a counter that wraps from 0x00 to 0xFF.

    Size of data shouldn't be more than maximum block size 
    supported by ECU (known with RequestDownload). 
    """
    
    __slots__ = ('block_sequence_counter', 'data',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.TRANSFER_DATA

    def __init__(self, block_sequence_counter, data:bytes):
        self.block_sequence_counter = block_sequence_counter
        self.data                   = data
        
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X36)
        [1:2]: Block sequence counter
        [2:N]: Data (bytes)
        """

        b = bytearray()

        b.extend(super(TransferData, self).__bytes__())
        b.extend(struct.pack("!B", self.block_sequence_counter))
        b.extend(self.data)

        return bytes(b)