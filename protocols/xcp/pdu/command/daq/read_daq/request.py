from xcp.enum.command_code import DataAcquisitionCommand

class ReadDaqRequest(object):

    def __init__(self):
        self._code = DataAcquisitionCommand.READ_DAQ