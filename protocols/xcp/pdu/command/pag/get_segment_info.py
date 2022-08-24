from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetSegmentInfoRequest(Cmd):
    PID = PageSwitchingCommand.GET_SEGMENT_INFO

    def __init__(self):
        self._mode           = 0xFF
        self._segment_number = 0xFF
        self._segment_info   = 0xFF
        self._mapping_index  = 0xFF

class GetSegmentInfoResponse(Res):
    PID = StandardCommandCode.CONNECT

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