from ctypes import c_uint8

from xcp.enum.command_code import CalibrationCommandCode
from xcp.enum.error_code import ErrorCode

from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.err import Err

class DownloadNext(Cmd):
    PID = CalibrationCommandCode.DOWNLOAD_NEXT

    def __init__(self, number_of_data_element = 0xFF, alignment = b'', data = b''):
        self.number_of_data_element = number_of_data_element
        self.alignment              = alignment
        self.data_element           = data

    def __bytes__(self):
        # TODO: Fill payload accordingly to spec
        class Payload(Cmd):
            PID = DownloadNext.PID
            
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

class DownloadNextResponse(Err):
    
    _pack_ = 1
    _fields_ =  [
                    ('code', c_uint8),
                    ('number_of_data_element', c_uint8),
                ]

    def __init__(self, code = ErrorCode.ERR_SEQUENCE, number_of_expected_data_element = 0xFF):
        self.code                            = code
        self.number_of_expected_data_element = number_of_expected_data_element