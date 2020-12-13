from xcp.enum.command_code import StandardCommandCode

class DisconnectRequest(object):
    """
    This class describes a disconnect request.
    """

    def __init__(self):
        self._code = StandardCommandCode.DISCONNECT