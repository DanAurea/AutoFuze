import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestUpload(ServiceBase):
    """
    Service allowing to read the downloaded firmware from ECU.
    """

    def __init__(self, memory_address = 0x0000, memory_size = 0x0000):
        self.service_id     = ServiceID.REQUEST_UPLOAD
        
        self.memory_address = memory_address # Mandatory field
        self.memory_size    = memory_size # Mandatory field
        
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X35)
        [1:N]: Memory address
        [N:M]: Memory size
        """

        b = bytearray()

        b.extend(super(RequestDownload, self).__bytes__())

        # TODO: Implement request upload logic

        return bytes(b)