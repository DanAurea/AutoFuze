import enum
import struct

from ctypes import c_uint8, c_uint16

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class IOControlByID(ServiceBase):

    __slots__ = ('did', 'parameter', 'option_record', 'enable_mask_record') # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.INPUT_OUTPUT_CONTROL_BY_IDENTIFIER
    
    class Parameter(enum.IntEnum):
        RETURN_CONTROL_TO_ECU  = 0x00
        RESET_TO_DEFAULT       = 0x01
        FREEZE_CURRENT_STATE   = 0x02
        SHORT_TERM_ADJUSTEMENT = 0x03

    def __init__(self, did = 0x0000, parameter = Parameter.RETURN_CONTROL_TO_ECU, option_record = b'', enable_mask_record = b''): 
        self.did                = did
        self.parameter          = parameter
        self.option_record      = option_record
        self.enable_mask_record = enable_mask_record

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2F)
        [1:2] : DID
        [2:3] : IO Control Parameter
        [3:N] : Control state (optinal)
        [N:M] : Control mask (optional)
        """
        option_record_format = 0 * c_uint8

        if self.parameter == self.Parameter.SHORT_TERM_ADJUSTEMENT:
            option_record_format = len(self.option_record) * c_uint8

        class Payload(ServiceBase):
            SERVICE_ID = IOControlByID.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('did', c_uint16),
                            ('parameter', c_uint8),
                            ('option_record', option_record_format),
                            ('enable_mask_record', len(self.enable_mask_record) * c_uint8),
                        ]

        payload = Payload()
        payload.did       = self.did
        payload.parameter = self.parameter

        if self.parameter == self.Parameter.SHORT_TERM_ADJUSTEMENT and len(self.option_record):
            payload.option_record[:len(self.option_record)] = self.option_record

        if self.enable_mask_record:
            payload.enable_mask_record = self.enable_mask_record

        return bytes(payload)

    def __repr__(self):
        s = """{}
                DID : 0x{:04X}
                Parameter : {}
                Option record : {}
                Enable mask record : {}
            """.format  (
                            super(IOControlByID, self).__repr__(),
                            self.did,
                            self.Parameter(self.parameter).name,
                            [hex(b) for b in self.option_record],
                            [hex(b) for b in self.enable_mask_record],
                        )

        return s