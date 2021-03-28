import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class TransferData(ServiceBase):

    def __init__(self, block_sequence_counter, data:bytes):
        self.service_id             = ServiceID.TRANSFER_DATA
        
        self.block_sequence_counter = block_sequence_counter
        self.data                   = data
        
    def __bytes__(self):
        pass