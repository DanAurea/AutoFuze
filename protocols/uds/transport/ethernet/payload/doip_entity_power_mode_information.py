from ctypes import c_uint8

from uds.transport.ethernet.enum.diagnostic_power_mode import DiagnosticPowerMode
from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class DoIPEntityPowerModeRequest(DoIPMessage):
    """
    """
    _pack_  =   1
    _fields =   [
                ]

    def __init__(self):
        super(DoIPEntityPowerModeRequest, self).__init__(payload_type = DoIPPayloadType.DIAGNOSTIC_POWER_MODE_INFORMATION_REQUEST)

class DoIPEntityPowerModeResponse(DoIPMessage):
    """
    """
    _pack_  =   1
    _fields =   [
                    ("diagnostic_power_mode", c_uint8)
                ]

    def __init__(self):
        super(DoIPEntityPowerModeResponse, self).__init__(payload_type = DoIPPayloadType.DIAGNOSTIC_POWER_MODE_INFORMATION_RESPONSE)

    def __repr__(self):
        s = """{}\rPayload:
                    \r\tDiagnostic power mode: {}
            """.format  (
                            super(DoIPEntityPowerModeResponse, self).__repr__(),
                            DiagnosticPowerMode(self.diagnostic_power_mode).name,
                        )

        return s