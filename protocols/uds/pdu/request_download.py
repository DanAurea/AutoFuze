import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestDownload(ServiceBase):
    """
    Service allowing to start a download between tester and ECU.
    Commonly used for flash updates.
    """

    def __init__(self, data_format = 0x00, parameters_length = 0x44, memory_address = 0x00, memory_size = 0x00): 
        self.service_id            = ServiceID.REQUEST_DOWNLOAD
        
        self.data_format           = data_format # [0:4] Encyrption method; [4:8] Compression method
        
        self.length_memory_address = parameters_length & 0xFF
        self.length_memory_size    = (parameters_length >> 4 ) & 0xFF
        
        self.memory_address        = memory_address
        self.memory_size           = memory_size

    def __bytes__(self):
        pass