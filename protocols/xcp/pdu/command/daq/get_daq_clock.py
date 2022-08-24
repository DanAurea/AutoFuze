from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqClockRequest(Cmd):
    PID = DataAcquisitionCommand.GET_DAQ_CLOCK

class GetDaqClockResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._receive_timestamp = 0xFF