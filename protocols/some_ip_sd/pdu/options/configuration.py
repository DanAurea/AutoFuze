from ctypes import BigEndianStructure, c_uint8, c_uint16

from protocols.some_ip_sd.pdu.option import Option

class ConfigurationOption(Option):
    _pack_      =   1
    _fields_    =   [
                        ("reserved", c_uint8),
                        # ("configuration_string", x * c_char), # Variable size (should inspect option length)
                    ]