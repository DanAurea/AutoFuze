from xcp.enum.command_code import StandardCommandCode
from xcp.enum.connect_mode import ConnectMode

class ConnectRequest(object):
    """
    This class describes a connect request.
    """
    def __init__(self):
        self._code = StandardCommandCode.CONNECT
        self._mode = ConnectMode.NORMAL_MODE