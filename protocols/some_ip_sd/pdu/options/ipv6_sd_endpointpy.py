from ctypes import BigEndianStructure, c_uint8, c_uint16, c_uint32

from protocols.some_ip_sd.pdu.option import Option

class IPv6SDEndpointOption(Option):
    _pack_      =   1
    _fields_    =   [
                        ("reserved", c_uint8), # Shall be set to 0x00
                        ("ipv6_address", 4 * c_uint32), # Unicast IP V6 address
                        ("reserved_2", c_uint8), # Shall be set to 0x00
                        ("transport_protocol", c_uint8), # Based on IANA / IETF types, 0x11 UDP
                        ("transport_protocol_port", c_uint16), # Shall be set to the port of the layer 4 protocol
                    ]