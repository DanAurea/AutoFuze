from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.parameter_bit import SetDaqListModeBit

class SetDaqListModeRequest(object):
    
    def __init__(self):
        self._code                        = DataAcquisitionCommand.SET_DAQ_LIST_MODE
        self._mode                        = SetDaqListModeBit(0xFF)
        self._daq_list_number             = 0xFF
        self._event_channel_number        = 0xFF
        self._transmission_rate_prescaler = 0xFF
        self._daq_list_priority           = 0xFF