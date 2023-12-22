from ctypes import BigEndianStructure

class XCPPacketBase(BigEndianStructure):
    
    def __new__(cls, *args, **kwargs):
        instance                = super(XCPPacketBase, cls).__new__(cls, *args, **kwargs)
        instance.identification = b'' # Identification is empty by default
        instance.timestamp      = b'' # Timestamp is empty by default

        return instance

    def is_correct_pid(self):
        return True

    def __bytes__(self):
        p = bytes(self.identification) + bytes(self.timestamp) + bytearray(self)
        return bytes(p)