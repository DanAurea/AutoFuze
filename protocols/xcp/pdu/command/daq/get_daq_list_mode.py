from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import GetDaqListModeBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqListModeRequest(Cmd):
    PID = DataAcquisitionCommand.GET_DAQ_LIST_MODE
    
    def __init__(self):
        self._daq_list_number = 0xFF

class GetDaqListModeResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._mode                 = GetDaqListModeBit(0xFF)
        self._event_channel_number = 0xFF
        self._prescaler            = 0xFF
        self._daq_list_number      = 0xFF