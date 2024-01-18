from ctypes import c_uint8

from xcp.enum.command_code import NvmProgrammingCommandCode
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import PgmPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetPgmProcessorInfo(Cmd):
    PID = NvmProgrammingCommandCode.GET_PGM_PROCESSOR_INFO
    
class GetPgmProcessorInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    _pack_   = 1
    _fields_ =  [
                    ('pgm_properties', c_uint8),
                    ('max_sector', c_uint8),
                ]

    def __init__(self, pgm_properties = PgmPropertiesBit(0xFF), max_sector = 0xFF):
        self.pgm_properties = pgm_properties
        self.max_sector     = max_sector