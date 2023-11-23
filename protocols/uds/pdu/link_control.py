import enum
import struct

from ctypes import c_uint8, c_uint16

from uds.enum.baudrate import BaudRate
from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class LinkControl(ServiceBase):
    """
    Service that control link status.
    """

    __slots__ = ('sub_function', 'link_control_id', 'link_record') # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.LINK_CONTROL

    class SubFunction(enum.IntEnum):
        VERIFY_TRANSITION_FIXED_PARAMETER    = 0x01
        VERIFY_TRANSITION_SPECIFIC_PARAMATER = 0x02
        TRANSITION_MODE                      = 0x03

    def __init__(self, sub_function = SubFunction.VERIFY_TRANSITION_FIXED_PARAMETER, link_control_id = 0x00, link_record = 0x00000): 
        self.sub_function    = sub_function
        self.link_control_id = link_control_id
        self.link_record     = link_record

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x87)
        [1:2] : Sub function
        [2:N] : Parameter (optional)
        """
        link_control_id_format = 0 * c_uint8
        
        if self.sub_function == self.SubFunction.VERIFY_TRANSITION_FIXED_PARAMETER:
            link_control_id_format = c_uint16        
        
        link_record_format = 0 * c_uint8
        
        if self.sub_function == self.SubFunction.VERIFY_TRANSITION_SPECIFIC_PARAMATER:
            link_record_format = 3 * c_uint8

        class Payload(ServiceBase):
            SERVICE_ID = LinkControl.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('sub_function', c_uint8),
                            ('link_control_id', link_control_id_format),
                            ('link_record', link_record_format),
                        ]

        payload = Payload()
        payload.sub_function    = self.sub_function

        if self.sub_function == self.SubFunction.VERIFY_TRANSITION_FIXED_PARAMETER:
            payload.link_control_id = self.link_control_id

        if self.sub_function == self.SubFunction.VERIFY_TRANSITION_SPECIFIC_PARAMATER:
            payload.link_record[0] = (self.link_record >> 16) & 0xFF
            payload.link_record[1] = (self.link_record >> 8) & 0xFF
            payload.link_record[2] = self.link_record & 0xFF

        return bytes(payload)

    def __repr__(self):
        s = """{}
                Sub function: {}
                Link control ID: 0x{:04X}
                Link record: 0x{:06X}
            """.format  (
                            super(LinkControl, self).__repr__(),
                            self.SubFunction(self.sub_function).name,
                            self.link_control_id,
                            self.link_record,
                        )

        return s