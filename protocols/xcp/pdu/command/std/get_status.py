from ctypes import c_uint8, c_uint16

from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import CurrentSessionStatusBit, RessourceBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetStatusRequest(Cmd):
    """
    This class describes a get current session request.
    """
    PID = StandardCommandCode.GET_STATUS

class GetStatusResponse(Res):
    """
    This class describes a get current session request.
    """
    PID = StandardCommandCode.CONNECT

    _pack_   = 1
    _fields_ =  [
                    ('session_status', c_uint8),
                    ('resource_protection_status', c_uint8),
                    ('reserved', c_uint8),
                    ('session_configuration_id', c_uint16),
                ]

    def __init__(self, session_status = CurrentSessionStatusBit(0xFF), resource_protection_status = RessourceBit(0xFF), session_configuration_id = 0xFF):
        self.session_status             = session_status
        self.resource_protection_status = resource_protection_status
        self.session_configuration_id   = session_configuration_id