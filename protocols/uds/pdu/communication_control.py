import enum
import struct

from ctypes import c_uint8, c_uint16

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class CommunicationControl(ServiceBase):
    """
    Service that set communication state, ECU reception/transmission of
    requests can be controlled with this one.
    Can be used to disable transmission of some answer during critical
    process (flash etc...)
    """

    __slots__ = ('sub_function', 'communication_type', 'node_id') # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.COMMUNICATION_CONTROL

    class SubFunction(enum.IntEnum):
        ENABLE_RX                               = ENABLE_TX = 0x00
        DISABLE_TX                              = 0x01
        DISABLE_RX                              = 0x02
        DISABLE_TX_ENHANCED_ADDRESS_INFORMATION = 0x04
        ENHANCED_ADDRESS_INFORMATION            = 0x05

    class CommunicationType(enum.IntEnum):
        NORMAL_MESSAGE                   = 0x01
        NETWORK_MANAGEMENT_MESSAGE       = 0x02
        # TODO : Set subnet values
        # DISABLE_SUBNET = 0x10 # 10 - E0
        DISABLE_RECEIVED_REQUEST_NETWORK = 0xF0

    def __init__(self, sub_function = SubFunction.ENABLE_RX | SubFunction.ENABLE_TX, communication_type = CommunicationType.NORMAL_MESSAGE, node_id = 0x0000): 
        self.sub_function       = sub_function
        self.communication_type = communication_type
        self.node_id            = node_id

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : SERVICE_ID (0x85)
        [1:2] : Sub function
        [2:3] : Communication type
        [3:5] : Node id (optional)
        """

        node_id_format = 0 * c_uint8
        
        if self.sub_function == self.SubFunction.DISABLE_TX_ENHANCED_ADDRESS_INFORMATION or self.sub_function == self.SubFunction.ENHANCED_ADDRESS_INFORMATION:
            node_id_format = c_uint16

        class Payload(ServiceBase):
            SERVICE_ID = CommunicationControl.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('sub_function', c_uint8),
                            ('communication_type', c_uint8),
                            ('node_id', node_id_format),
                        ]

        payload = Payload()
        payload.sub_function       = self.sub_function
        payload.communication_type = self.communication_type

        if self.sub_function == self.SubFunction.DISABLE_TX_ENHANCED_ADDRESS_INFORMATION or self.sub_function == self.SubFunction.ENHANCED_ADDRESS_INFORMATION:
            payload.node_id            = self.node_id

        return bytes(payload)

    def __repr__(self):
        s = """{}
            Sub function: {}
            CommunicationType: {}
            Node ID: 0x{:04X}
            """.format  (
                            super(CommunicationControl, self).__repr__(),
                            self.SubFunction(self.sub_function).name,
                            self.CommunicationType(self.communication_type).name,
                            self.node_id,
                        )

        return s