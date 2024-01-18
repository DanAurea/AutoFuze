from ctypes import c_uint8

from xcp.enum.command_code import PageSwitchCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSegmentInfo(Cmd):
    PID = PageSwitchCommandCode.GET_SEGMENT_INFO

    _pack_   = 1
    _fields_ =  [
                    ('mode', c_uint8),
                    ('segment_number', c_uint8),
                    ('segment_info', c_uint8),
                    ('mapping_index', c_uint8),
                ]

    def __init__(self, mode = 0xFF, segment_number = 0xFF, segment_info = 0xFF, mapping_index = 0xFF):
        self.mode           = mode
        self.segment_number = segment_number
        self.segment_info   = segment_info
        self.mapping_index  = mapping_index

class GetSegmentInfoResponse(Res):
    PID = StandardCommandCode.CONNECT

    # TODO: Handle different positive responses

    def __init__(self):        
        """
        Mode = 0
        """
        self._basic_info         = 0xFF
        
        """
        Mode = 1
        """
        self._max_pages          = 0xFF
        self._address_extension  = 0xFF
        self._max_mapping        = 0xFF
        self._compression_method = 0xFF
        self._encryption_method  = 0xFF
        
        """
        Mode = 2
        """
        self._mapping_info        = 0xFF