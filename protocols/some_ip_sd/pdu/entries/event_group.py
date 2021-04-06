from ctypes import BigEndianStructure, c_uint8, c_uint16, c_uint32

class EventGroupEntry(BigEndianStructure):
    _pack_   =  1
    _fields_ =  [
                    ("type", c_uint8),
                    ("index_first_options", c_uint8),
                    ("index_second_options", c_uint8),
                    ("number_options_1", c_uint8, 4),
                    ("number_options_2", c_uint8, 4),
                    ("service_id", c_uint16),
                    ("instance_id", c_uint16),
                    ("major_version", c_uint8),
                    ("ttl", 3 * c_uint8),
                    ("reserved", c_uint8),
                    ("flags", c_uint8, 4),
                    ("counter", c_uint8, 4),
                    ("event_group_id", c_uint16),
                ]