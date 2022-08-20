import enum
import struct

from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.enum.session import Session
from uds.pdu.base import ServiceBase

class SessionControl(ServiceBase):
    """
    Service allowing to switch of session type to unlock services only
    present in specific session.
    """
    __slots__ = ('session',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.DIAGNOSTIC_SESSION_CONTROL

    _pack_   = 1
    _fields_ =  [
                    ('_session', c_uint8)
                ]

    def __init__(self, session = Session.DEFAULT_SESSION):
        self.session  = self._session = session

    def __repr__(self):
        s = """{}
                Session: {}
            """.format  (
                            super(SessionControl, self).__repr__(),
                            self.session.name,
                        )

        return s