from xcp.enum.command_code import DataAcquisitionCommand
from xcp.enum.command_code import StandardCommandCode
from xcp.pdu.cto.cmd import Cmd
from xcp.pdu.cto.res import Res

class ReadDaqRequest(Cmd):
    PID = DataAcquisitionCommand.READ_DAQ

class ReadDaqResponse(Res):
    PID = StandardCommandCode.CONNECT

    def __init__(self):
        self._bit_offset          = 0xFF
        self._size_of_daq_element = 0xFF
        self._address_extension   = 0xFF
        self._address             = 0xFF