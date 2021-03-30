import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class CommunicationControl(ServiceBase):
    """
    Service that set communication state, ECU reception/transmission of
    requests can be controlled with this one.
    Can be used to disable transmission of some answer during critical
    process (flash etc...)
    """

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.COMMUNICATION_CONTROL
    
    class SubFunction(enum.IntEnum):
        ENABLE = 0x01

    class Communication(enum.IntEnum):
        ENABLE_RX  = ENABLE_TX = 0x00
        DISABLE_TX = 0x01
        DISABLE_RX = 0x02

    def __init__(self, sub_function = SubFunction.ENABLE, communication = Communication.ENABLE_TX): 
        self.sub_function = sub_function

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : Service ID (0x28)
        [1:2] : Sub function
        """

        b = bytearray()

        b.extend(super(CommunicationControl, self).__bytes__())
        b.extend(struct.pack("!B", self.sub_function))

        return bytes(b)

    def __repr__(self):
        s = """{}
            Sub function: {}
            """.format  (
                            super(CommunicationControl, self).__repr__(),
                            self.sub_function.name,
                        )

        return s