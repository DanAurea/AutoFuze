import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class SessionControl(ServiceBase):
    """
    Service allowing to switch of session type to unlock services only
    present in specific session.
    """

    __slots__ = ('session',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.DIAGNOSTIC_SESSION_CONTROL
    
    class Session(enum.IntEnum):
        DEFAULT_SESSION                  = 0x01
        PROGRAMMING_SESSION              = 0x02
        EXTENDED_DIAGNOSTIC_SESSION      = 0x03
        SAFETY_SYSTEM_DIAGNOSTIC_SESSION = 0x04
        # OEM SPECIFIC SESSION >= 0x05

    def __init__(self, session = Session.DEFAULT_SESSION):
        self.session    = session
        
    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x10)
        [1:2] : Session
        """

        b = bytearray()

        b.extend(super(SessionControl, self).__bytes__())
        b.extend(struct.pack("!B", self.session))

        return bytes(b)

    def __repr__(self):
        s = """{}
                Session: {}
            """.format  (
                            super(SessionControl, self).__repr__(),
                            self.session.name,
                        )

        return s