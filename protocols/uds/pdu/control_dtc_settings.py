import enum
import struct

from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ControlDTCSettings(ServiceBase):
    """
    Control DTC policy.
    """

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.CONTROL_DTC_SETTINGS
    
    class SubFunction(enum.IntEnum):
        ON  = 0x01
        OFF = 0x02

    def __init__(self, sub_function = SubFunction.ON, settings = []): 
        self.sub_function = sub_function
        self.settings     = settings

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x85)
        [1:2] : Sub function
        [2:N] : Settings (optional)
        """
        class Payload(ServiceBase):
            SERVICE_ID = ControlDTCSettings.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('sub_function', c_uint8),
                            ('settings', len(self.settings) * 3 * c_uint8),
                        ]

        payload = Payload()
        payload.sub_function = self.sub_function

        # TODO: Check if there's not a more elegant way to proceed on.
        for i, dtc in enumerate(self.settings):
            payload.settings[3*i]       = (dtc >> 16) & 0xFF
            payload.settings[(3*i) + 1] = (dtc >> 8) & 0xFF
            payload.settings[(3*i) + 2] = dtc & 0xFF

        return bytes(payload)

    def __repr__(self):
        s = """{}
                Sub function: {}
                DTC settings: {}
            """.format  (
                            super(ControlDTCSettings, self).__repr__(),
                            self.sub_function.name,
                            [hex(b) for b in self.settings],
                        )

        return s