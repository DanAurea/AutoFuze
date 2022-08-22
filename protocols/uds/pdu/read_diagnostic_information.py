import enum
import struct

from ctypes import c_uint8

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class ReadDiagnosticInformation(ServiceBase):
    """
    Service that allows to read ECU's DTC that has been triggered during
    runtime because of some issues happening (faults).
    """
    
    __slots__ = ('dtc', 'record_number', 'status_mask', 'sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID   = ServiceID.READ_DTC_INFORMATION

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
        REPORT_DTC_EXTENDED_DATA_RECORD_BY_RECORD_NUMBER                            = 0X16

    def __init__(self, sub_function = SubFunction.REPORT_DTC_SNAPSHOT, dtc = 0x000000, record_number = 0x00, status_mask = 0x00): 
        self.sub_function  = sub_function
        self.dtc           = dtc
        self.record_number = record_number
        self.status_mask   = status_mask

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x19)
        [1:2] : Sub function
        [2:5] : DTC
        """
        class PayloadBase(ServiceBase):
            SERVICE_ID = ReadDiagnosticInformation.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('sub_function', c_uint8),
                        ]


        # TODO: Some request could be missing or being incorrect, check further.
        if self.sub_function in [self.SubFunction.REPORT_DTC_EXTENDED_DATA_RECORD_BY_DTC_NUMBER, 
                                   self.SubFunction.REPORT_MIRROR_MEMORY_DTC_EXTENDED_DATA_RECORD_BY_DTC_NUMBER,
                                   self.SubFunction.REPORT_DTC_SNAPSHOT_BY_DTC,
                                   ]:
            class Payload(PayloadBase):
                _pack_   = 1
                _fields_ =  [
                                ('dtc', 3 * c_uint8),
                                ('record_number', c_uint8),
                            ]

            payload = Payload()
            payload.dtc[0] = (self.dtc >> 16) & 0xFF
            payload.dtc[1] = (self.dtc >> 8) & 0xFF
            payload.dtc[2] = self.dtc & 0xFF
            payload.record_number = self.record_number

        elif self.sub_function in [self.SubFunction.REPORT_DTC_SNAPSHOT_BY_RECORD_NUMBER,
                                   self.SubFunction.REPORT_DTC_EXTENDED_DATA_RECORD_BY_RECORD_NUMBER,
                                   ]:
            class Payload(PayloadBase):
                _pack_   = 1
                _fields_ =  [
                                ('record_number', c_uint8),
                            ]

            payload = Payload()
            payload.record_number = self.record_number

        elif self.sub_function == self.SubFunction.REPORT_SEVERITY_INFORMATION_OF_DTC:
            class Payload(PayloadBase):
                _pack_   = 1
                _fields_ =  [
                                ('dtc', c_uint8),
                            ]

            payload = Payload()
            payload.dtc[0] = (self.dtc >> 16) & 0xFF
            payload.dtc[1] = (self.dtc >> 8) & 0xFF
            payload.dtc[2] = self.dtc & 0xFF
        elif self.sub_function in [self.SubFunction.REPORT_DTC_BY_SEVERITY_MASK_RECORD, 
                                   self.SubFunction.REPORT_NUMBER_OF_DTC_BY_SEVERITY_MASK_RECORD,
                                   self.SubFunction.REPORT_EMISSIONS_RELATED_OBD_DTC_BY_STATUS_MASK,
                                   self.SubFunction.REPORT_NUMBER_OF_EMISSIONS_RELATED_OBD_DTC_BY_STATUS_MASK,
                                   self.SubFunction.REPORT_NUMBER_OF_MIRROR_MEMORY_DTC_BY_STATUS_MASK,
                                   ]:
            class Payload(PayloadBase):
                _pack_   = 1
                _fields_ =  [
                                ('status_mask', c_uint8),
                            ]

            payload = Payload()
            payload.status_mask = self.status_mask

        else:
            class Payload(PayloadBase):
                _pack_   = 1
                _fields_ =  []

            payload = Payload()
        
        payload.sub_function = self.sub_function

        return bytes(payload)

    def __repr__(self):
        s = """{}
        Sub function: {}
        DTC: 0x{:06X}
        Record number: 0x{:02X}
        Status mask: 0x{:02X}
        """.format  (
                    super(ReadDiagnosticInformation, self).__repr__(),
                    self.SubFunction(self.sub_function).name,
                    self.dtc,
                    self.record_number,
                    self.status_mask,
                )

        return s