import enum

from ctypes import c_char, c_uint8, c_uint16, c_uint32, c_uint64

from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class RequestFileTransfer(ServiceBase):
        
    __slots__ = ('mode', 'file_path_name_length', 'file_path_name', 'data_format', 'file_size_length', 'file_size_uncompressed', 'file_size_compressed')

    SERVICE_ID = ServiceID.REQUEST_FILE_TRANSFER
    
    class Mode(enum.IntEnum):
        ADD_FILE     = 0X01
        DELETE_FILE  = 0X02
        REPLACE_FILE = 0X03
        READ_FILE    = 0X04
        READ_DIR     = 0X05

    def __init__(self, mode = Mode.ADD_FILE, file_path_name_length = 1, file_path_name = '0', data_format = 0x00, file_size_length = 1, file_size_uncompressed = 0x00, file_size_compressed = 0x00):
        self.mode                   = mode
        self.file_path_name_length  = file_path_name_length
        self.file_path_name         = file_path_name
        self.data_format            = data_format # [0:4] Encyrption method; [4:8] Compression method
        self.file_size_length       = file_size_length
        self.file_size_uncompressed = file_size_uncompressed
        self.file_size_compressed   = file_size_compressed

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1]: Service ID (0X38)
        [1:2]: Mode
        [2:4]: File path and name length
        [4:N]: File path and name
        [N:N+1]: Data format (Encyrption method / Compression method)
        [N+1:N+2]: File size length
        [N+2:N+2+M]: File size uncompressed
        [N+2+M:N+2+2M]: File size compressed
        """
        ctypes_data_format = 0 * c_uint8

        if self.mode != self.Mode.DELETE_FILE and self.mode != self.Mode.READ_DIR:
            ctypes_data_format = c_uint8
        
        file_size_length_format = 0 * c_uint8
        file_size_format        = 0 * c_uint8

        if self.mode != self.Mode.DELETE_FILE and self.mode != self.Mode.READ_DIR and self.mode != self.Mode.READ_FILE:
            file_size_length_format = c_uint8
            
            if self.file_size_length == 1:
                file_size_format        = c_uint8
            elif self.file_size_length == 2:
                file_size_format        = c_uint16
            elif self.file_size_length == 4:
                file_size_format        = c_uint32
            elif self.file_size_length == 8:
                file_size_format        = c_uint64

        class Payload(ServiceBase):
            SERVICE_ID = RequestFileTransfer.SERVICE_ID
            _pack_   = 1
            _fields_ =  [
                            ('mode', c_uint8),
                            ('file_path_name_length', c_uint16),
                            ('file_path_name', self.file_path_name_length * c_char),
                            ('data_format', ctypes_data_format),
                            ('file_size_length', file_size_length_format),
                            ('file_size_uncompressed', file_size_format),
                            ('file_size_compressed', file_size_format),
                        ]

        payload = Payload()
        payload.mode                                        = self.mode
        payload.file_path_name_length                       = self.file_path_name_length
        payload.file_path_name = self.file_path_name.encode('ascii')

        if self.mode != self.Mode.DELETE_FILE and self.mode != self.Mode.READ_DIR:
            payload.data_format = self.data_format

        if self.mode != self.Mode.DELETE_FILE and self.mode != self.Mode.READ_DIR and self.mode != self.Mode.READ_FILE:
            payload.file_size_length       = self.file_size_length   
            payload.file_size_uncompressed = self.file_size_uncompressed
            payload.file_size_compressed   = self.file_size_compressed

        return bytes(payload)

    def __repr__(self):
        s = """{}
            Mode: {}
            File path and name length: {}
            File path and name: {}
            Data format: 0x{:04X}
            File size length: {}
            File size uncompressed: 0x{:08X}
            File size compressed: 0x{:08X}
            """.format  (
                        super(RequestFileTransfer, self).__repr__(),
                        self.Mode(self.mode).name,
                        self.file_path_name_length,
                        self.file_path_name,
                        self.data_format,
                        self.file_size_length,
                        self.file_size_uncompressed,
                        self.file_size_compressed,
                    )

        return s