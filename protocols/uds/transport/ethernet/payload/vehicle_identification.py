from ctypes import c_char, c_uint8

from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class VehicleIdentification(DoIPMessage):
    _pack_   = 1
    _fields_ =  [
                ]

    def __init__(self):
        super(VehicleIdentification, self).__init__(payload_type = DoIPPayloadType.VEHICLE_IDENTIFICATION_REQUEST)

class VehicleIdentificationEID(DoIPMessage):
    _pack_   = 1
    _fields_ =  [
                    ("eid", 6 * c_uint8)
                ]

    def __init__(self, eid):
        super(VehicleIdentificationEID, self).__init__(payload_type = DoIPPayloadType.VEHICLE_IDENTIFICATION_REQUEST_EID)
        self.eid = eid
    
    def __repr__(self):
        s = """{}\rPayload:
                 \r\tEID : {}
            """.format  (
                            super(VehicleIdentificationEID).__repr__(),
                            ":".join([b for b in self.eid]), # MAC address
                        )

        return s

class VehicleIdentificationVIN(DoIPMessage):
    _pack_   = 1
    _fields_ =  [
                    ("vin", 17 * c_char)
                ]

    def __init__(self, vin):
        super(VehicleIdentificationVIN, self).__init__(payload_type = DoIPPayloadType.VEHICLE_IDENTIFICATION_REQUEST_VIN)
        self.vin = bytes(vin.encode('ascii')) # TODO: Handle this with EBCDIC instead of ascii

    def __repr__(self):
        s = """{}\rPayload:
                 \r\tVIN : {}
            """.format  (
                            super(VehicleIdentificationVIN, self).__repr__(),
                            "".join([chr(c) for c in self.vin]),
                        )

        return s
