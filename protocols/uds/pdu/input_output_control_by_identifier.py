import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class IOControlByID(ServiceBase):

    __slots__ = ('ecu_id', 'parameter',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.INPUT_OUTPUT_CONTROL_BY_IDENTIFIER
    
    class Parameter(enum.IntEnum):
        RETURN_CONTROL_TO_ECU  = 0x00
        RESET_TO_DEFAULT       = 0x01
        FREEZE_CURRENT_STATE   = 0x02
        SHORT_TERM_ADJUSTEMENT = 0x03

    def __init__(self, ecu_id = 0x00, parameter = Parameter.RETURN_CONTROL_TO_ECU): 
        self.ecu_id      = ecu_id
        self.parameter   = parameter

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
        b.extend(struct.pack("!B", self.parameter))

        return bytes(b)