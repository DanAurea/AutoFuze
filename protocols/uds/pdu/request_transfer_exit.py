import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestTransferExit(ServiceBase):
    SERVICE_ID = ServiceID.REQUEST_TRANSFER_EXIT