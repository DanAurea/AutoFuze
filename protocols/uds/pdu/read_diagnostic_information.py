import enum
import struct

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadDiagnosticInformation(ServiceBase):
    """
    Service that allows to read ECU's DTC that has been triggered during
    runtime because of some issues happening (faults).
    """

    class SubFunction(enum.IntEnum):
        REPORT_NUMBER_OF_DTC                                        = 0X01
        REPORT_DTC                                                  = 0X02
        REPORT_DTC_SNAPSHOT                                         = 0X03
        REPORT_DTC_SNAPSHOT_BY_DTC                                  = 0X04
        REPORT_DTC_SNAPSHOT_BY_RECORD_NUMBER                        = 0X05
        REPORT_DTC_EXTENDED_DATA_RECORD_BY_DTC_NUMBER               = 0X06
        REPORT_NUMBER_OF_DTC_BY_SEVERITY_MASK_RECORD                = 0X07
        REPORT_DTC_BY_SEVERITY_MASK_RECORD                          = 0X08
        REPORT_SEVERITY_INFORMATION_OF_DTC                          = 0X09
        REPORT_SUPPORTED_DTC                                        = 0X0A
        REPORT_FIRST_TEST_FAILED_DTC                                = 0X0B
        REPORT_FIRST_CONFIRMED_DTC                                  = 0X0C
        REPORT_MOST_RECENT_TEST_FAILED_DTC                          = 0X0D
        REPORT_MOST_RECENT_TEST_CONFIRMED_DTC                       = 0X0D
        REPORT_MOST_RECENT_CONFIRMED_DTC                            = 0X0E
        REPORT_MIRROR_MEMORY_DTC                                    = 0X0F
        REPORT_MIRROR_MEMORY_DTC_EXTENDED_DATA_RECORD_BY_DTC_NUMBER = 0X10
        REPORT_NUMBER_OF_MIRROR_MEMORY_DTC_BY_STATUS_MASK           = 0X11
        REPORT_NUMBER_OF_EMISSIONS_RELATED_OBD_DTC_BY_STATUS_MASK   = 0X12
        REPORT_EMISSIONS_RELATED_OBD_DTC_BY_STATUS_MASK             = 0X13
        REPORT_DTC_FAULT_DETECTION_COUNTER                          = 0X14
        REPORT_DTC_WITH_PERMANENT_STATUS                            = 0X15

    def __init__(self, sub_function = SubFunction.REPORT_DTC_SNAPSHOT, dtc = 0x000000, record = 0x00): 
        self.service_id   = ServiceID.READ_DTC_INFORMATION
        self.sub_function = sub_function
        self.dtc          = dtc
        self.record       = record

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x19)
        [1:2] : Sub function
        [2:5] : DTC
        """
        b = bytearray()

        b.extend(super(ReadDiagnosticInformation, self).__bytes__())
        b.extend(struct.pack("!B", self.sub_function))

        # TODO: Implement Read DTC crafting depending on sub function (record etc...)

        return bytes(b)