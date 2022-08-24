from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class WriteDaqRequest(Cmd):
    PID = DataAcquisitionCommand.WRITE_DAQ
    
    def __init__(self):
        self._bit_offset          = 0xFF
        self._size_of_daq_element = 0xFF
        self._address_extension   = 0xFF
        self._address             = 0xFF