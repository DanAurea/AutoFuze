from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetDaqListInfoBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqListInfo(Cmd):
    PID = DataAcquisitionCommandCode.GET_DAQ_LIST_INFO
    
    _pack_   = 1
    _fields_ =  [
                    ('reserved', c_uint8),
                    ('daq_list_number', c_uint16),
                ]

    def __init__(self, daq_list_number = 0xFF):
        self.daq_list_number = daq_list_number

class GetDaqListInfoResponse(Res):
    PID = StandardCommandCode.CONNECT

    _pack_   = 1
    _fields_ =  [
                    ('daq_list_properties', c_uint8),
                    ('max_odt', c_uint8),
                    ('max_odt_entries', c_uint8),
                    ('fixed_event', c_uint16),
                ]
    
    def __init__(self, daq_list_properties = GetDaqListInfoBit(0xFF), max_odt = 0xFF, max_odt_entries = 0xFF, fixed_event = 0xFF):
        self.daq_list_properties = daq_list_properties
        self.max_odt             = max_odt
        self.max_odt_entries     = max_odt_entries
        self.fixed_event         = fixed_event