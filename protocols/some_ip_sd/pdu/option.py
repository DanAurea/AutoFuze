from ctypes import BigEndianStructure, c_uint8, c_uint16

class Option(BigEndianStructure):
    _pack_      =   1
    _fields_    =   [
                        ("length", c_uint16),
                        ("type", c_uint8),
                    ]