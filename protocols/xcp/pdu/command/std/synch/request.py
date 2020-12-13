from xcp.enum.command_code import StandardCommandCode

class SynchRequest(object):
    """
    This class describes a connect request.
    """
    def __init__(self):
        self._code = StandardCommandCode.SYNCH