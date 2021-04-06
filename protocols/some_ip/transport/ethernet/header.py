from ctypes import BigEndianStructure, c_uint8, c_uint32

class SOMEIPHeader(BigEndianStructure):
    _pack_      =   1
    _fields_    =   [
                        ("message_id", c_uint32), # Service ID (16 bits) / 0 if method, 1 if event (1 bit) / Method or Event ID (last 15 bits)
                        ("length", c_uint32), # Length of next fields (including payload)

                        ("request_id", c_uint32), # Client ID (16 bits) / Session ID (16 bits) 
                        ("protocol_version", c_uint8), # Default is 0x01
                        ("interface_version", c_uint8), # Allows debugging tools to identify service interface used
                        ("message_type", c_uint8),
                        ("return_code", c_uint8),
                        #("payload", x * c_ubyte) # Payload of variable size
                    ] 
