from ctypes import c_uint8

from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

class DownloadRequest(Cmd):
    PID = CalibrationCommandCode.DOWNLOAD

    def __init__(self, number_of_data_element = 0xFF, alignment = b'', data = b''):
        self.number_of_data_element = number_of_data_element
        self.alignment              = alignment
        self.data_element           = data

    def __bytes__(self):
        class Payload(Cmd):
            PID = DownloadRequest.PID

            _pack_   = 1
            _fields_ =  [
                            ('number_of_data_element', c_uint8),
                            ('alignment', self.number_of_data_element * c_uint8),
                            ('data_element', len(self.data_element) * c_uint8),
                        ]

        payload = Payload()
        payload.number_of_data_element = self.number_of_data_element
        payload.alignment              = (self.number_of_data_element * c_uint8)(*self.alignment)
        payload.data_element           = (len(self.data_element) * c_uint8)(*self.data_element)

        return bytes(payload)