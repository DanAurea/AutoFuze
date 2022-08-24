from xcp.enum.command_code import CalibrationCommandCode
from xcp.pdu.cto.cmd import Cmd

from struct import pack

class DownloadRequest(Cmd):
    PID = CalibrationCommandCode.DOWNLOAD

    def __init__(self, number_of_data_element = 0xFF, alignment = 0xFF, data = bytearray()):
        self._number_of_data_element = number_of_data_element
        self._alignment              = alignment
        self._data_element           = data

    def __bytes__(self):
        cmd_bytes = bytearray()

        parameters = pack("<BBB", self.pid, self._number_of_data_element, self._alignment)
        cmd_bytes.extend(parameters)
        cmd_bytes.extend(self._data_element)

        return bytes(cmd_bytes)