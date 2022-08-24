from ctypes import c_uint8

from xcp.pdu.base import XCPPacketBase

class XCPCTOCodeBase(XCPPacketBase):
    _pack_   = 1
    _fields_ =  [
                    ('code', c_uint8),
                ]

    def __new__(cls, *args, **kwargs):
        instance             = super(XCPCTOBase, cls).__new__(cls, *args, **kwargs)
        instance.code = cls.CODE
        return instance