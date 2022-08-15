from ctypes import BigEndianStructure, c_uint8

class OBDIIFrameBase(BigEndianStructure):
    _pack_   = 1
    _fields_ = [
                ("number_byte", c_uint8),
                ("mode", c_uint8),
                ("pid", c_uint8),
                ("payload", 4 * c_uint8) #Payload content                
                ("unused", c_uint8)                
                ]