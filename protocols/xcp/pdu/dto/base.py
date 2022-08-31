from xcp.pdu.base import XCPPacketBase
from xcp.pdu.identification import Identification
from xcp.pdu.timestamp import Timestamp

class XCPDTOBase(XCPPacketBase):
    def __new__(cls, pid = None, fill = False, daq = None, daq_word = False, timestamp_value = None, timestamp_length = 1, *args, **kwargs):
        instance                = super(XCPPacketBase, cls).__new__(cls, *args, **kwargs)
        instance.identification = Identification(pid, fill, daq, daq_word)
        instance.timestamp      = Timestamp(timestamp_value, timestamp_length) # Timestamp is empty in CMD

        return instance