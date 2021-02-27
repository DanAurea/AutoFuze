from ctypes import *
from enum.protocol_version import DoIPProtocolVersion
from enum.payload_type import DoIPPayloadType

class DoIPHeader(BigEndianStructure):
    """
    This class describes a DoIP header.
    """
    _fields_ =  [
                    ("protocol_version", c_uint8),
                    ("inverse_protocol_version", c_uint8),
                    ("payload_type", c_uint16),
                    ("payload_length", c_uint32)
                ]

    def __repr__(self):
        header =    '''
                        DoIP Header:
                        \t Protocol version: {} 
                        \t Inverse protocol version: {} 
                        \t Payload type: {} 
                        \t Payload length: {} bytes
                    '''.format  (
                                    str(DoIPProtocolVersion(self.protocol_version)),
                                    hex(self.inverse_protocol_version & 0xFF),
                                    str(DoIPPayloadType(self.payload_type)),
                                    str(self.payload_length)
                                )

        return header 