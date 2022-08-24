from xcp.enum.command_code import PageSwitchingCommand
from xcp.enum.parameter_bit import SetSegmentModeBit
from xcp.pdu.cto.cmd import Cmd

class SetSegmentModeRequest(Cmd):
    PID = PageSwitchingCommand.SET_SEGMENT_MODE

    def __init__(self):
        self._mode           = SetSegmentModeBit(0xFF)
        self._segment_number = 0xFF