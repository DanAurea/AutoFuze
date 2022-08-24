from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.parameter_bit import DaqKeyBit, DaqPropertiesBit
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class GetDaqProcessorInfoRequest(Cmd):
    PID = DataAcquisitionCommand.GET_DAQ_PROCESSOR_INFO

class GetDaqProcessorInfoResponse(Res):
    PID = DataAcquisitionCommand.CONNECT

    def __init__(self):
        self._daq_properties    = DaqPropertiesBit(0xFF)
        self._max_daq           = 0xFF
        self._max_event_channel = 0xFF
        self._min_daq           = 0xFF
        self._daq_key_byte      = DaqKeyBit(0xFF)