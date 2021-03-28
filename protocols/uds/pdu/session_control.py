import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class SessionControl(ServiceBase):

    class Session(enum.IntEnum):
        DEFAULT_SESSION     = 0x01
        PROGRAMMING_SESSION = 0x02
        EXTENDED_DIAGNOSTIC_SESSION = 0x02

    def __init__(self, session = self.Session.DEFAULT_SESSION):
        self.service_id = ServiceID.DIAGNOSTIC_SESSION_CONTROL
        self.session    = session        
        
    def __bytes__(self):
        pass