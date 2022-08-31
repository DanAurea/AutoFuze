from ctypes import c_uint8

from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class UploadRequest(Cmd):
    PID = StandardCommandCode.UPLOAD
    
    _pack_   = 1
    _fields_ =  [
                    ('number_of_data_element', c_uint8),
                ]

    def __init__(self, number_of_data_element = 0xFF):
        self.number_of_data_element = 0xFF

class UploadResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self, number_of_data_element, alignment = b'', elements  = b''):
        self.number_of_data_element = number_of_data_element
        self.alignment              = alignment
        self.elements               = elements

    def __bytes__(self):
        class Payload(Res):
            PID = UploadResponse.PID
            
            _pack_   = 1
            _fields_ =  [
                            ('alignment', self.number_of_data_element * c_uint8),
                            ('elements', len(self.elements) * c_uint8),
                        ]

        payload = Payload()
        payload.alignment = (self.number_of_data_element * c_uint8)(*self.alignment)
        payload.elements  = (len(self.elements) * c_uint8)(*self.elements)

        return bytes(payload)