from xcp.enum.command_code import StandardCommandCode

class GetSegmentInfoResponse(object):

    def __init__(self):
        self._code               = StandardCommandCode.CONNECT
        
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