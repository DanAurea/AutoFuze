from ctypes import LittleEndianStructure, c_uint8

class XCPPacketBase(LittleEndianStructure):
    PID = 0x00
    
    _pack_   = 1
    _fields_ =  [
                    ('pid', c_uint8),
                ]

    def __new__(cls, *args, **kwargs):
        instance             = super(XCPPacketBase, cls).__new__(cls, *args, **kwargs)
        instance.pid = cls.PID
        return instance

    def is_correct_pid(self):
        return True