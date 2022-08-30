from ctypes import c_uint8

from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class DownloadMaxRequest(Cmd):
    PID = CalibrationCommandCode.DOWNLOAD_MAX

    def __init__(self, alignment = b'', data_elements = b''):
        self.alignment     = alignment
        self.data_elements = data_elements
    
    def __bytes__(self):
        class Payload(Cmd):
            _pack_   = 1
            _fields_ =  [
                            ('alignment', len(self.alignment) * c_uint8),
                            ('data_element', len(self.data_element) * c_uint8),
                        ]

        payload = Payload()
        payload.alignment              = (len(self.alignment) * c_uint8)(*self.alignment)
        payload.data_element           = (len(self.data_element) * c_uint8)(*self.data_element)

        return bytes(payload)