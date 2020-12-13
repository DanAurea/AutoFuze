from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.parameter_bit import DaqKeyBit, DaqPropertiesBit

class GetDaqProcessorInfoResponse(object):

    def __init__(self):
        self._code              = DataAcquisitionCommand.CONNECT
        self._daq_properties    = DaqPropertiesBit(0xFF)
        self._max_daq           = 0xFF
        self._max_event_channel = 0xFF
        self._min_daq           = 0xFF
        self._daq_key_byte      = DaqKeyBit(0xFF)