import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class SecurityAccess(ServiceBase):

    class SubFunction(enum.IntEnum):
        REQUEST_SEED = 0x01
        SEND_KEY     = 0x02

    def __init__(self, sub_function = self.SubFunction.REQUEST_SEED, key = None):
        self.service_id   = ServiceID.SECURITY_ACCESS
        self.sub_function = sub_function        
        self.key          = key
        
    def __bytes__(self):
        pass