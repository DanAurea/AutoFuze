from xcp.enum.command_code import StandardCommandCode

class GetStatusRequest(object):
    """
    This class describes a get current session request.
    """

    def __init__(self):
        self._code = StandardCommandCode.GET_STATUS