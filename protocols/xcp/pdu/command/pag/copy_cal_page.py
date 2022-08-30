from ctypes import c_uint8

from xcp.enum.command_code import PageSwitchingCommand
from xcp.pdu.cto.cmd import Cmd

class CopyCalPageRequest(Cmd):
    PID = PageSwitchingCommand.COPY_CAL_PAGE

    _pack_   = 1
    _fields_ =  [
                    ('logical_data_segment_number_source', c_uint8),
                    ('logical_data_page_number_source', c_uint8),
                    ('logical_data_segment_number_destination', c_uint8),
                    ('logical_data_page_number_destination', c_uint8),
                ]

    def __init__(self, logical_data_segment_number_source = 0xFF, logical_data_page_number_source = 0xFF, logical_data_segment_number_destination = 0xFF, logical_data_page_number_destination = 0xFF):
        self.logical_data_segment_number_source      = logical_data_segment_number_source
        self.logical_data_page_number_source         = logical_data_page_number_source
        self.logical_data_segment_number_destination = logical_data_segment_number_destination
        self.logical_data_page_number_destination    = logical_data_page_number_destination