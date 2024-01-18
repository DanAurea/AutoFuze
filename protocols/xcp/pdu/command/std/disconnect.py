from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd

class Disconnect(Cmd):
    """
    This class describes a disconnect request.
    """
    PID = StandardCommandCode.DISCONNECT