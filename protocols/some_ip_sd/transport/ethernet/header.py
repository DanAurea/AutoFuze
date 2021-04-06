from ctypes import c_uint8, c_uint32

from protocols.some_ip.enum.message_type import MessageType
from protocols.some_ip.enum.return_code import ReturnCode
from protocols.some_ip.transport.ethernet.header import SOMEIPHeader

class SOMEIPSDHeader(SOMEIPHeader):
    _pack_      =   1
    _fields_    =   [
                        # Inherits from header

                        # ("message_id", c_uint32), # Service ID (16 bits) / 0 if method, 1 if event (1 bit) / Method or Event ID (last 15 bits)
                        # ("length", c_uint32), # Length of next fields (including payload)

                        # ("request_id", c_uint32), # Client ID (16 bits) / Session ID (16 bits) 
                        # ("protocol_version", c_uint8), # Default is 0x01
                        # ("interface_version", c_uint8), # Allows debugging tools to identify service interface used
                        # ("message_type", c_uint8),
                        # ("return_code", c_uint8),
                        
                        ("flags", c_uint8),
                        ("reserved", 3 * c_uint8),
                        ("length_entries_array", c_uint32),
                        # ("entries_array", x * c_ubyte) # Variable size
                        # ("length_options_array", c_uint32)
                        # ("options_array", x * c_ubyte) # Variable size
                    ]

    SOME_IP_SD_MESSAGE_ID = 0xFFFF8100

    def __init__(self):
        self.message_id        = self.SOME_IP_SD_MESSAGE_ID
        
        self.protocol_version  = 0x01
        self.interface_version = 0x01
        self.message_type      = MessageType.NOTIFICATION
        self.return_code       = ReturnCode.E_OK

    def entries_array(self):
        pass    

    def options_array(self):
        pass