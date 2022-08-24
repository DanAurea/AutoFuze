from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.enum.parameter_bit import TimestamModeBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqResolutionInfoRequest(Cmd):
    PID = DataAcquisitionCommand.DAQ_RESOLUTION_INFO

class GetDaqResolutionInfoResponse(Res):
    PID = StandardCommandCode.CONNECT
    
    def __init__(self):
        self._granularity_odt_entry_size_daq  = 0xFF
        self._max_odt_entry_size_daq          = 0xFF
        self._granularity_odt_entry_size_stim = 0xFF
        self._max_odt_entry_size_stim         = 0xFF
        self._timestamp_mode                  = TimestamModeBit(0xFF)
        self._timestamp_ticks                 = 0xFF