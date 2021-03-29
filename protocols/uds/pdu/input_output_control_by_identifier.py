import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class IOControlByID(ServiceBase):

    class Parameter(enum.IntEnum):
        NONE                   = 0x00
        RETURN_CONTROL_TO_ECU  = 0x01
        RESET_TO_DEFAULT       = 0x02
        FREEZE_CURRENT_STATE   = 0x03
        SHORT_TERM_ADJUSTEMENT = 0x04

    def __init__(self, ecu_id = 0x00, parameter = Parameter.NONE): 
        self.service_id = ServiceID.INPUT_OUTPUT_CONTROL_BY_IDENTIFIER
        self.ecu_id     = ecu_id
        self.parameter  = parameter

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2F)
        [1:N] : ECU ID
        [N:3] : Parameter (optional)
        """

        b = bytearray()

        b.extend(super(IOControlByID, self).__bytes__())

        # TODO: Compute number of bytes used by ECU ID
        b.extend(struct.pack("!" + "B", self.ecu_id))
        
        if self.parameter != self.Parameter.NONE:
            b.extend(struct.pack("!B", self.parameter))

        return bytes(b)