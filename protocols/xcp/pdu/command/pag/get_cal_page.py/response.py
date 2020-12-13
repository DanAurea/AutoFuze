from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import SetCalPageBit

class GetCalPageResponse(object):
    
    def __init__(self):
        self._code                     = StandardCommandCode.CONNECT
        self._logical_data_page_number = 0xFF