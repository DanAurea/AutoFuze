import sys
sys.path.append("../../")
sys.path.append("../../protocols")

from protocols.xcp.enum.command_code import CalibrationCommandCode
from protocols.xcp.pdu.command.cal.download import DownloadRequest
from protocols.xcp.transport.can import CanTransport
from protocols.xcp.transport.ethernet import EthernetTransport
from struct import unpack

"""
DISCLAIMER: This only a simple test made as a primary usage of XCP API but more tests should be done in future to ensure good code testability.
"""

data         = b"\x00\xf0\xf2\xf2"
download_req = DownloadRequest(number_of_data_element = len(data), alignment = 0x01, data = bytearray(data))

xcp_packet = bytes(download_req)

command_code, number_of_data_element, alignment = unpack("<3B", xcp_packet[:3])
data_unpack                                     = unpack("<4B", xcp_packet[3:])

# Check that xcp packet contains correct data
assert command_code           == CalibrationCommandCode.DOWNLOAD
assert number_of_data_element == len(data)
assert alignment              == 0x01
assert bytearray(data)        == bytearray(data_unpack)

eth_transport = EthernetTransport()
eth_frame_1   = eth_transport.create_message((xcp_packet))
eth_frame_2   = eth_transport.create_message((xcp_packet))

# Check that eth frame is correctly formed
assert unpack("<H", eth_frame_1[:2])[0]  == 0x07
assert unpack("<H", eth_frame_1[2:4])[0] == 0x00
assert unpack("<H", eth_frame_2[2:4])[0] == 0x01

can_transport = CanTransport()
can_frame     = can_transport.create_message((xcp_packet))

# Check that can frame is correctly formed when fill is not enabled
assert unpack("<B", can_frame[:1])[0] == 0x07

# Check that can frame is correctly formed when fill is enabled
can_transport = CanTransport(should_fill = True)
can_frame     = can_transport.create_message((xcp_packet))

assert unpack("<B", can_frame[:1])[0] == 0x08
assert len(can_frame[1:]) == 0x08