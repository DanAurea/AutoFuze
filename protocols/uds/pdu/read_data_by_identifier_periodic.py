import enum
import struct

from ctypes import c_uint8, c_uint16, BigEndianStructure, LittleEndianStructure

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadDataByIDPeriodic(ServiceBase):
    """
    Service that read a data into ECU's memory by referring to a Data ID (DID) periodically.
    """
    __slots__ = ('did_list', 'mode',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID = ServiceID.READ_DATA_BY_IDENTIFIER_PERIODIC
    
    class TransmissionMode(enum.IntEnum):
        SEND_AT_SLOW_RATE   = 0X01
        SEND_AT_MEDIUM_RATE = 0X02
        SEND_AT_FAST_RATE   = 0X03
        STOP_SENDING        = 0X04

    def __init__(self, mode = TransmissionMode.SEND_AT_MEDIUM_RATE, did_list = []): 
        self.mode       = mode
        self.did_list   = did_list

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x2A)
        [1:2] : Transmission mode (DID)
        [2:N] : Periodic DID (optional)
        """
        class Payload(ServiceBase):
            SERVICE_ID = ReadDataByIDPeriodic.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('mode', c_uint8),
                            ('did_list', len(self.did_list) * c_uint16),
                        ]

        payload = Payload()
        payload.mode = self.mode

        if self.did_list:
            payload.did_list[:len(self.did_list)] = self.did_list

        return bytes(payload)

    def __repr__(self):
        s = """{}
                Transmission mode: {}
                DID list: {}
            """.format  (
                            super(ReadDataByIDPeriodic, self).__repr__(),
                            self.TransmissionMode(self.mode).name,
                            [hex(b) for b in  self.did_list]
                        )

        return s