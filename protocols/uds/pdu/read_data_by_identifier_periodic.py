import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadDataByIDPeriodic(ServiceBase):
    """
    Service that read a data into ECU's memory by referring to a Data ID (DID) periodically.
    """

    __slots__ = ('did', 'mode',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.READ_DATA_BY_IDENTIFIER_PERIODIC
    
    class TransmissionMode(enum.IntEnum):
        SEND_AT_SLOW_RATE   = 0X01
        SEND_AT_MEDIUM_RATE = 0X02
        SEND_AT_FAST_RATE   = 0X03
        STOP_SENDING        = 0X04

    def __init__(self, mode = TransmissionMode.SEND_AT_MEDIUM_RATE, did = 0x0000): 
        self.mode       = mode
        self.did        = did

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2A)
        [1:3] : Data ID (DID)
        """

        b = bytearray()

        # TODO: Check if logic is fullfilled or if there's something left required.
        b.extend(super(ReadDataByIDPeriodic, self).__bytes__())
        b.extend(struct.pack("!B", self.mode))
        b.extend(struct.pack("!H", self.did))

        return bytes(b)