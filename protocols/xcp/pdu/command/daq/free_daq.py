from xcp.enum.command_code import DataAcquisitionCommand
from xcp.pdu.cto.cmd import Cmd

class FreeDaqRequest(Cmd):
    PID = DataAcquisitionCommand.FREE_DAQ