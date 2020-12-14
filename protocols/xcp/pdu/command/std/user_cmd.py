from xcp.enum.command_code import StandardCommandCode

class UserCmdRequest(object):
    """
    This class describes a connect request.
    """
    def __init__(self):
        self._code             = StandardCommandCode.USER_CMD
        self._sub_command_code = 0xFF
        self._parameters       = bytearray()