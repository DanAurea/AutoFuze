from xcp.enum.command_code import DataAcquisitionCommand

class GetDaqProcessorInfoRequest(object):

    def __init__(self):
        self._code = DataAcquisitionCommand.GET_DAQ_PROCESSOR_INFO