from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class StartStopDaqListRequest(Cmd):
    PID = DataAcquisitionCommand.START_STOP_DAQ_LIST
    
    def __init__(self):
        self._mode            = 0xFF
        self._daq_list_number = 0xFF

class StartStopDaqListResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._first_pid = 0xFF