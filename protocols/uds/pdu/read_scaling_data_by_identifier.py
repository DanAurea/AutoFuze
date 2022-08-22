import enum

from ctypes import c_uint16

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadScalingDataByID(ServiceBase):

    __slots__ = ('did',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID   = ServiceID.READ_SCALING_DATA_BY_IDENTIFIER
    
    _pack_   = 1
    _fields_ =  [
                    ('did', c_uint16),
                ] 

    def __init__(self, did = 0x0000): 
        self.did = did

    def __repr__(self):
        s = """{}
                DID: 0x{:04X}
            """.format  (
                            super(ReadScalingDataByID, self).__repr__(),
                            self.did
                        )

        return s