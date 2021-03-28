import enum

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadDiagnosticInformation(ServiceBase):

    class SubFunction(enum.IntEnum):
        REPORT_NUMBER_OF_DTC                          = 0X01
        REPORT_DTC                                    = 0X02
        REPORT_DTC_SNAPSHOT                           = 0X03
        REPORT_DTC_SNAPSHOT_BY_DTC                    = 0X04
        REPORT_DTC_SNAPSHOT_BY_RECORD_NUMBER          = 0X05
        REPORT_DTC_EXTENDED_DATA_RECORD_BY_DTC_NUMBER = 0X06
        REPORT_NUMBER_OF_MIRROR_MEMORY_DTC            = 0X11
        REPORT_MIRROR_MEMORY_DTC                      = 0X0F

    def __init__(self, sub_function = self.SubFunction.REPORT_DTC_SNAPSHOT, dtc = 0x000000, record = 0x00): 
        self.service_id   = ServiceID.READ_DTC_INFORMATION
        self.sub_function = sub_function
        self.dtc          = dtc
        self.record       = record

    def __bytes__(self):
        pass