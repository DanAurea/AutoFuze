from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ClearDiagnosticInformation(ServiceBase):
    """
    Service that clears fault of a defined DTC.
    """

    __slots__ = ('dtc_group',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.CLEAR_DIAGNOSTIC_INFORMATION
    
    def __init__(self, dtc_group = 0x000000):
        self.dtc_group = dtc_group

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : Service ID
        [1:4] : DTC
        """
        class Payload(ServiceBase):
            SERVICE_ID = ClearDiagnosticInformation.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('dtc_group', 3 * c_uint8),
                        ]

        payload = Payload()

        # TODO: Check if there's not a more elegant way to proceed on.
        payload.dtc_group[0] = (self.dtc_group >> 16) & 0xFF
        payload.dtc_group[1] = (self.dtc_group >> 8) & 0xFF
        payload.dtc_group[2] = self.dtc_group & 0xFF

        return bytes(payload)

    def __repr__(self):
        s = """{}
                DTC group: 0x{:06X}
            """.format  (
                            super(ClearDiagnosticInformation, self).__repr__(),
                            self.dtc_group,
                        )

        return s