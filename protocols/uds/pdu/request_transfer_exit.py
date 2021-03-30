import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestTransferExit(ServiceBase):

    SERVICE_ID = ServiceID.REQUEST_TRANSFER_EXIT
        
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X37)
        """
        return super(RequestTransferExit, self).__bytes__()                        