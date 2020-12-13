from xcp.enum.command_code import StandardCommandCode

class SetMtaRequest(object):
    
    def __init__(self):
        self._code              = StandardCommandCode.SET_MTA
        self._address_extension = 0xFF
        self._address           = 0xFF