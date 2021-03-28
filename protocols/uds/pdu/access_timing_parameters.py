from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class AccsTimingParameters(ServiceBase):

    def __init__(self, sub_function = 0x0): 
        self.service_id   = ServiceID.ACCESS_TIMING_PARAMETERS
        self.sub_function = sub_function

    def __bytes__(self):
        pass