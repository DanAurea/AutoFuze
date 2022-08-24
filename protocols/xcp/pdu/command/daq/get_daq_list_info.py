from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import DaqListPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqListInfoRequest(Cmd):
    PID = DataAcquisitionCommand.GET_DAQ_LIST_INFO
    
    def __init__(self):
        self._daq_list_number = 0xFF

class GetDaqListInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._daq_list_properties = DaqListPropertiesBit(0xFF)
        self._max_odt             = 0xFF
        self._max_odt_entires     = 0xFF
        self._fixed_event         = 0xFF