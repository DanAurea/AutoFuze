from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ClearDiagnosticInformation(ServiceBase):
    """
    Service that clears fault of a defined DTC.
    """

    __slots__ = ('dtc',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.CLEAR_DIAGNOSTIC_INFORMATION
    
    def __init__(self, dtc = 0x000000):
        self.dtc         = dtc

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : Service ID
        [1:4] : DTC
        """
        b = bytearray()

        # Convert to big endian (network endianness)
        b.extend(super(ClearDiagnosticInformation, self).__bytes__())
        b.extend(struct.pack('!3B', self.dtc))

        return bytes(b)

    def __repr__(self):
        s = """{}
                DTC: {}
            """.format  (
                            super(ClearDiagnosticInformation, self).__repr__(),
                            self.dtc,
                        )

        return s