from xcp.enum.command_code import DataAcquisitionCommandCode
from xcp.pdu.cto.cmd import Cmd

class FreeDaq(Cmd):
    PID = DataAcquisitionCommandCode.FREE_DAQ