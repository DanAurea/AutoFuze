from ctypes import c_char, c_uint8, c_uint16

from uds.transport.ethernet.enum.connection_kind import ConnectionKind
from uds.transport.ethernet.enum.further_action_required import FurtherActionRequired
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.enum.vin_gid_sync_status import VINGIDSyncStatus
from uds.transport.ethernet.message import DoIPMessage

class VehicleAnnouncement(DoIPMessage):
    """
    Message sent from ECU when booting. ECU will send 3 announcement
    messages at each boot (reset included).
    
    This message give information about ECU and allows to identify it on
    a multiplexed bus.
    """
    _pack_ = 1
    _fields_ =  [
                    ("VIN", 17 * c_char), # Vehicle Identification Number
                    ("logical_address", c_uint16), # DoIP Logical address
                    ("EID", 6 * c_uint8), # MAC address
                    ("GID", 6 * c_uint8), # Can be different depending on ECU configuration
                    ("further_action_required", c_uint8), # Define if any further action is required (routing activation for instance)
                    ("VIN_GID_sync_status", c_uint8), # Status of synchronization between VIN and GID (Optional)
                ]

    CONNECTION_KIND = ConnectionKind.UDP
    PAYLOAD_TYPE    = DoIPPayloadType.VEHICLE_ANNOUNCEMENT_MESSAGE
    
    def __init__(self, vin = "0123456789ABCDEFG", logical_address = 0x00, eid = 0x001122334455, gid = 0x01122334455, further_action_required = FurtherActionRequired.ROUTING_ACTIVATION_REQUIRED, vin_gid_sync_status = VINGIDSyncStatus.VIN_GID_NOT_SYNCHRONIZED):
        super(VehicleAnnouncement, self).__init__()
        self.vin                     = bytes(vin.encode("ascii")) # TODO: Handle this as EBCDIC instead of ASCII
        self.logical_address         = logical_address
        self.eid                     = eid
        self.gid                     = gid
        self.further_action_required = further_action_required
        self.vin_gid_sync_status     = vin_gid_sync_status

    def __repr__(self):

        eid = '{:012x}'.format(self.eid).upper() # TODO: Should be handled differently
        gid = '{:012x}'.format(self.gid).upper() # TODO: Should be handled differently

        s = """{}\rPayload:
                 \r\tVIN : {}
                 \r\tlogical address : {}
                 \r\tEID : {}
                 \r\tGID : {}
                 \r\tFurther action required : {}
                 \r\tVIN/GID sync status : {}
            """.format  (
                            super(VehicleAnnouncement, self).__repr__(),
                            "".join([chr(c) for c in self.vin]),
                            hex(self.logical_address),
                            ":".join(['{}{}'.format(b0, b1) for b0, b1 in zip(eid[0::2], eid[1::2])]), # TODO: Create an util function that convert int to mac
                            ":".join(['{}{}'.format(b0, b1) for b0, b1 in zip(gid[0::2], gid[1::2])]), # TODO: Create an util function that convert int to mac
                            FurtherActionRequired(self.further_action_required).name,
                            VINGIDSyncStatus(self.vin_gid_sync_status).name,
                        )

        return s