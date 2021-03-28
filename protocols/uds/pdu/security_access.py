import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class SecurityAccess(ServiceBase):
    """
    Service allowing to unlock secured services.

    Unlock process follows this sequence flow:
    
    Tester: Request seed
    ECU: Provide a seed
    Tester: Compute key from seed with a determined cipher (OEM dependent).
    Tester: Send back the key
    ECU: Answer with ACK/NACK 
    """

    class SubFunction(enum.IntEnum):
        REQUEST_SEED = 0x01
        SEND_KEY     = 0x02

    def __init__(self, sub_function = SubFunction.REQUEST_SEED, key = None):
        self.service_id   = ServiceID.SECURITY_ACCESS
        self.sub_function = sub_function        
        self.key          = key
        
    def __bytes__(self):
        pass