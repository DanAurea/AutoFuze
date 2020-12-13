from xcp.enum.command_code import DataAcquisitionCommand

class GetDaqEventInfoRequest(object):
    
    def __init__(self):
        self._code                 = DataAcquisitionCommand.GET_DAQ_EVENT_INFO
        self._event_channel_number = 0xFF