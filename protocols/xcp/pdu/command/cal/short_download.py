from ctypes import c_uint8, c_uint32

from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class ShortDownloadRequest(Cmd):
    PID = CalibrationCommandCode.SHORT_DOWNLOAD
    
    def __init__(self, number_of_data_element = 0xFF, address_extension = 0xFF, address = 0xFF, data_elements = b''):
        self.number_of_data_element = number_of_data_element
        self.address_extension      = address_extension
        self.address                = address
        self.data_elements          = data_elements

    def __bytes__(self):
        class Payload(Cmd):
            PID = ShortDownloadRequest.PID
            
            _pack_   = 1
            _fields_ =  [
                            ('number_of_data_element', c_uint8),
                            ('reserved', c_uint8),
                            ('address_extension', c_uint8),
                            ('address', c_uint32),
                            ('data_elements', len(self.data_elements) * c_uint8),
                        ]

        payload = Payload()
        payload.number_of_data_element = self.number_of_data_element
        payload.address_extension      = self.address_extension
        payload.address                = self.address
        payload.data_elements          = (len(self.data_elements) * c_uint8)(*self.data_elements)

        return bytes(payload)